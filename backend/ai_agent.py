import os
import json
import sqlite3
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "petshop.db")

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY", "your_groq_api_key_here"),
)

def _query_db(query, args=(), fetchall=True):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query, args)
        if fetchall:
            result = [dict(row) for row in cursor.fetchall()]
        else:
            row = cursor.fetchone()
            result = dict(row) if row else None
        conn.close()
        return result
    except Exception as e:
        return {"error": str(e)}

def buscar_produto(nome: str):
    """Busca produtos no pet shop por nome ou palavra-chave."""
    query = "SELECT nome, categoria, preco, descricao, estoque FROM produtos WHERE nome LIKE ?"
    result = _query_db(query, (f"%{nome}%",))
    if not result:
        return {"mensagem": f"Nenhum produto encontrado com '{nome}'."}
    return result

def buscar_servico(nome: str):
    """Busca serviços no pet shop por nome ou palavra-chave."""
    query = "SELECT nome, preco, descricao FROM servicos WHERE nome LIKE ?"
    result = _query_db(query, (f"%{nome}%",))
    if not result:
        return {"mensagem": f"Nenhum serviço encontrado com '{nome}'."}
    return result

def consultar_preco(item: str):
    """Consulta o preço de um produto ou serviço específico."""
    prod_query = "SELECT nome, preco, 'produto' as tipo FROM produtos WHERE nome LIKE ?"
    prods = _query_db(prod_query, (f"%{item}%",))
    
    serv_query = "SELECT nome, preco, 'servico' as tipo FROM servicos WHERE nome LIKE ?"
    servs = _query_db(serv_query, (f"%{item}%",))
    
    resultados = prods + servs
    if not resultados:
        return {"mensagem": f"Não encontramos preço para '{item}'."}
    return resultados

def consultar_horario():
    """Consulta os horários de funcionamento do pet shop em todos os dias da semana."""
    query = "SELECT dia_semana, abertura, fechamento FROM horarios"
    return _query_db(query)

# Mapear nomes de ferramentas para funções
available_tools = {
    "buscar_produto": buscar_produto,
    "buscar_servico": buscar_servico,
    "consultar_preco": consultar_preco,
    "consultar_horario": consultar_horario,
}

tools_definition = [
    {
        "type": "function",
        "function": {
            "name": "buscar_produto",
            "description": "Busca produtos no sistema do pet shop por nome ou palavra-chave (ex: ração, coleira, shampoo).",
            "parameters": {
                "type": "object",
                "properties": {
                    "nome": {
                        "type": "string",
                        "description": "O nome ou parte do nome do produto (ex: 'ração', 'premier')."
                    }
                },
                "required": ["nome"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "buscar_servico",
            "description": "Busca serviços oferecidos no pet shop por nome (ex: banho, tosa, consulta).",
            "parameters": {
                "type": "object",
                "properties": {
                    "nome": {
                        "type": "string",
                        "description": "O nome ou parte do nome do serviço (ex: 'banho', 'tosa')."
                    }
                },
                "required": ["nome"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "consultar_preco",
            "description": "Consulta o preço de um item, podendo ser produto ou serviço.",
            "parameters": {
                "type": "object",
                "properties": {
                    "item": {
                        "type": "string",
                        "description": "O nome do item (produto ou serviço) para consultar o preço."
                    }
                },
                "required": ["item"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "consultar_horario",
            "description": "Consulta os horários de funcionamento do pet shop para todos os dias.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    }
]

SYSTEM_PROMPT = """Você é o assistente virtual do Pet Mix, um pequeno pet shop.
Sua função é atender aos clientes, tirar dúvidas sobre produtos, preços, serviços e horários.
Utilize as ferramentas (function calling) disponíveis para consultar as informações atualizadas do sistema.
Se a informação não estiver na base de dados, DICA QUE NÃO SABE. Não invente produtos, serviços ou preços.
Seja educado, simpático e direto nas respostas.
Se o cliente tiver um perfil de pet (contexto), utilize isso para personalizar a resposta.
"""

def chat_with_agent(messages, pet_context=None):
    # Prepara mensagem do sistema
    system_msg = {"role": "system", "content": SYSTEM_PROMPT}
    if pet_context:
        system_msg["content"] += f"\nContexto do animal do cliente: Nome={pet_context.get('nome')}, Espécie={pet_context.get('especie')}, Porte={pet_context.get('porte')}."
    
    conversation = [system_msg] + messages

    response = client.chat.completions.create(
        model="qwen/qwen3.8-27b",
        messages=conversation,
        tools=tools_definition,
        tool_choice="auto",
        max_tokens=1024
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        # Adicionar a mensagem do assistente com chamadas de ferramenta à conversa
        conversation.append(response_message)
        
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_tools.get(function_name)
            
            if function_to_call:
                function_args = json.loads(tool_call.function.arguments)
                function_response = function_to_call(**function_args)
                
                conversation.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": json.dumps(function_response, ensure_ascii=False),
                    }
                )
        
        # Obter a resposta final do modelo
        second_response = client.chat.completions.create(
            model="qwen/qwen3.8-27b",
            messages=conversation,
            max_tokens=1024
        )
        return second_response.choices[0].message.content
    
    return response_message.content

