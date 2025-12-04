import sqlite3

# Conectar ao banco (se não existir, será criado)
conexao = sqlite3.connect("LiberiumStore.db")
cursor = conexao.cursor()

# ===============================
# TABELA LIVROS
# ===============================
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    livro_id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo_livro TEXT NOT NULL,
    escritor TEXT NOT NULL,
    preco_livro REAL NOT NULL,
    descricao_livro TEXT,
    pdf_livro BLOB,
    capa_livro BLOB
);
""")

# ===============================
# TABELA COMENTARIO
# ===============================
cursor.execute("""
CREATE TABLE IF NOT EXISTS comentario (
    comentario_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_leitor TEXT NOT NULL,
    comentario_leitor TEXT NOT NULL
);
""")

# ===============================
# TABELA CONTATO LEITOR
# ===============================
cursor.execute("""
CREATE TABLE IF NOT EXISTS contato_leitor (
    contato_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    nome TEXT,
    senha TEXT,
    telefone TEXT,
    mensagem TEXT
);
""")

# ===============================
# TABELA CONTATO ESCRITOR
# ===============================
cursor.execute("""
CREATE TABLE IF NOT EXISTS contato_escritor (
    contato_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    nome TEXT,
    senha TEXT,
    telefone TEXT,
    mensagem TEXT
);
""")

# ===============================
# TABELA PAGAMENTO
# ===============================
cursor.execute("""
CREATE TABLE IF NOT EXISTS pagamento (
    pagamento_id INTEGER PRIMARY KEY AUTOINCREMENT,
    leitor TEXT,
    livro_id INTEGER,
    metodo_pago TEXT,
    valor_pago REAL,
    data_pago TEXT,
    FOREIGN KEY (livro_id) REFERENCES livros (livro_id)
);
""")

# Salvar tudo
conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso!")
