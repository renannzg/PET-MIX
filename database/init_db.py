import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "petshop.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Cria tabelas
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

    # Limpar dados antigos, se houver
    cursor.execute('DELETE FROM produtos')
    cursor.execute('DELETE FROM servicos')
    cursor.execute('DELETE FROM horarios')

    # Inserir dados de exemplo
    produtos = [
        ('Ração Premier Cães Adultos 15kg', 'Alimentação', 189.90, 'Ração premium para cães adultos', 10),
        ('Ração Golden Gatos Castrados 3kg', 'Alimentação', 45.50, 'Ração para gatos castrados', 15),
        ('Shampoo Pet Sanol 500ml', 'Higiene', 22.90, 'Shampoo neutro para cães e gatos', 20),
        ('Coleira Antipulgas Seresto', 'Saúde', 250.00, 'Proteção prolongada contra pulgas e carrapatos', 5)
    ]
    cursor.executemany('INSERT INTO produtos (nome, categoria, preco, descricao, estoque) VALUES (?, ?, ?, ?, ?)', produtos)

    servicos = [
        ('Banho P', 40.00, 'Banho para cães de pequeno porte'),
        ('Banho M', 50.00, 'Banho para cães de médio porte'),
        ('Banho G', 60.00, 'Banho para cães de grande porte'),
        ('Tosa Higiênica', 35.00, 'Tosa das áreas íntimas e patas'),
        ('Consulta Veterinária', 120.00, 'Consulta clínica geral')
    ]
    cursor.executemany('INSERT INTO servicos (nome, preco, descricao) VALUES (?, ?, ?)', servicos)

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

    conn.commit()
    conn.close()
    print("Database initialized successfully at", DB_PATH)

if __name__ == "__main__":
    init_db()
