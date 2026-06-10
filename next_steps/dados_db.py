import sqlite3

DB_NAME = "biblioteca.db"

def inicializar_banco():
    """Cria a tabela caso ela não exista."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            isbn TEXT PRIMARY KEY,
            titulo TEXT NOT EXISTS,
            autor TEXT
        )
    """)
    conn.commit()
    conn.close()

def listar_livros():
    conn = sqlite3.connect(DB_NAME)
    # Transforma as linhas retornadas em dicionários automaticamente
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    linhas = cursor.fetchall()
    conn.close()
    return [dict(linha) for row in linhas]

def buscar_por_isbn(isbn):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros WHERE isbn = ?", (isbn,))
    linha = cursor.fetchone()
    conn.close()
    return dict(linha) if linha else None

def salvar_livro(livro):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO livros (isbn, titulo, autor) VALUES (?, ?, ?)",
                       (livro['isbn'], livro['titulo'], livro['autor']))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False # ISBN Duplicado
    finally:
        conn.close()

def deletar_livro(isbn):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livros WHERE isbn = ?", (isbn,))
    linhas_afetadas = cursor.rowcount
    conn.commit()
    conn.close()
    return linhas_afetadas > 0