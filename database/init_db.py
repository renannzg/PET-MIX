import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "petshop.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tabelas do sistema
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT,
        preco REAL,
        descricao TEXT,
        estoque INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS servicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL,
        descricao TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS horarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dia_semana TEXT NOT NULL,
        abertura TEXT,
        fechamento TEXT
    )
    ''')

    # Tabela de Políticas e Conhecimento (RAG Textual de Políticas do Estabelecimento)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS politicas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topico TEXT NOT NULL,
        conteudo TEXT NOT NULL,
        palavras_chave TEXT
    )
    ''')

    # Limpar dados antigos
    cursor.execute('DELETE FROM produtos')
    cursor.execute('DELETE FROM servicos')
    cursor.execute('DELETE FROM horarios')
    cursor.execute('DELETE FROM politicas')

    # Dados de Produtos
    produtos = [
        ('Ração Premier Cães Adultos 15kg', 'Alimentação', 189.90, 'Ração premium especial para cães adultos de médio e grande porte', 12),
        ('Ração Golden Gatos Castrados 3kg', 'Alimentação', 45.50, 'Ração premium balanceada para gatos adultos castrados sabor frango', 18),
        ('Ração Royal Canin Mini Puppy 2.5kg', 'Alimentação', 115.00, 'Alimento super premium para filhotes de cães de porte pequeno até 10 meses', 8),
        ('Shampoo Pet Sanol 500ml', 'Higiene', 22.90, 'Shampoo neutro hidratante com extrato de camomila para cães e gatos', 25),
        ('Coleira Antipulgas Seresto P/M', 'Saúde', 249.90, 'Proteção duradoura de até 8 meses contra pulgas e carrapatos em cães até 8kg', 6),
        ('Petisco Whiskas Temptations 85g', 'Petiscos', 9.50, 'Petisco crocante recheado sabor carne para gatos', 30),
        ('Brinquedo Mordedor Osso Nylon', 'Acessórios', 28.00, 'Brinquedo resistente atóxico para higiene bucal canina', 14)
    ]
    cursor.executemany('INSERT INTO produtos (nome, categoria, preco, descricao, estoque) VALUES (?, ?, ?, ?, ?)', produtos)

    # Dados de Serviços
    servicos = [
        ('Banho P', 40.00, 'Banho completo para cães de pequeno porte (até 10kg), inclui corte de unhas e limpeza de orelhas'),
        ('Banho M', 50.00, 'Banho completo para cães de médio porte (10kg a 25kg), com secagem e hidratação básica'),
        ('Banho G', 60.00, 'Banho completo para cães de grande porte (acima de 25kg), com secagem profunda'),
        ('Tosa Higiênica', 35.00, 'Aparação de pelos nas patas, genitais e barriga para maior higiene do pet'),
        ('Tosa Completa na Máquina', 75.00, 'Tosa geral padronizada com acabamento nas patas e focinho'),
        ('Consulta Veterinária Clínica', 120.00, 'Consulta com médico veterinário clínico geral para avaliação de rotina ou queixas')
    ]
    cursor.executemany('INSERT INTO servicos (nome, preco, descricao) VALUES (?, ?, ?)', servicos)

    # Horários de Funcionamento
    horarios = [
        ('Segunda-feira', '08:00', '18:00'),
        ('Terça-feira', '08:00', '18:00'),
        ('Quarta-feira', '08:00', '18:00'),
        ('Quinta-feira', '08:00', '18:00'),
        ('Sexta-feira', '08:00', '18:00'),
        ('Sábado', '09:00', '14:00'),
        ('Domingo', 'Fechado', 'Fechado')
    ]
    cursor.executemany('INSERT INTO horarios (dia_semana, abertura, fechamento) VALUES (?, ?, ?)', horarios)

    # Base de Conhecimento: Políticas e Dúvidas Frequentes (RAG)
    politicas = [
        (
            'Vacinação e Requisitos para Banho e Tosa',
            'Para a segurança de todos os pets, é obrigatório apresentar a carteira de vacinação em dia (V8/V10 e Antirrábica para cães; Quádrupla e Antirrábica para gatos). Pets com pulgas/carrapatos ativos recebem aplicação preventiva obrigatória no ato.',
            'vacina vacinas vacinacao carteirinha regras banho tosa requisitos doenca'
        ),
        (
            'Agendamento e Cancelamento de Serviços',
            'Os serviços de banho e tosa exigem agendamento prévio por telefone ou mensagem. Tolerância máxima de atraso de 15 minutos. Cancelamentos ou reagendamentos devem ser feitos com no mínimo 2 horas de antecedência.',
            'agendar agendamento horario marcar cancelar reagendar atraso'
        ),
        (
            'Formas de Pagamento e Parcelamento',
            'Aceitamos PIX, dinheiro e cartões de crédito e débito das principais bandeiras (Visa, Mastercard, Elo, Hipercard). Parcelamos compras a partir de R$ 150,00 em até 3x sem juros.',
            'pagamento pix cartao debito credito parcelamento parcelar dinheiro juros'
        ),
        (
            'Tele-entrega e Delivery',
            'Realizamos tele-entrega de rações e produtos para bairros próximos no mesmo dia para pedidos até às 15:00. Taxa de entrega fixa de R$ 8,00, ou frete grátis para compras acima de R$ 120,00.',
            'entrega delivery frete tele entrega envio receber em casa'
        ),
        (
            'Política de Trocas e Devoluções',
            'Produtos lacrados em embalagem original podem ser trocados em até 7 dias corridos após a compra com comprovante. Rações abertas possuem garantia de 100% de satisfação do fabricante conforme política de cada marca.',
            'troca trocar devolucao devolver garantia defeito racao aberta'
        ),
        (
            'Aviso de Limitação e Saúde Animal',
            'O assistente virtual fornece informações comerciais, preços e regras do Pet Mix. Em situações de emergência médica, sintomas clínicos, intoxicação ou dor do animal, procure imediatamente um médico veterinário presencial.',
            'veterinario saude remedio doente vomito veneno dor sangue emergencia medicamento'
        )
    ]
    cursor.executemany('INSERT INTO politicas (topico, conteudo, palavras_chave) VALUES (?, ?, ?)', politicas)

    conn.commit()
    conn.close()
    print("Database initialized successfully at", DB_PATH)

if __name__ == "__main__":
    init_db()
