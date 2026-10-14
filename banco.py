import sqlite3

nome = "usuarios.db"
def cadastrar_usuario(nome_usuarios, email, senha):
    sql = "INSERT INTO usuarios (nome, email, senha) VALUES (?,?,?)"

    try:
        with sqlite3.connect(nome) as conn:

            # Cria um cursor
            cur = conn.cursor()

            # Executa o script passando as variáveis recebidas na função
            cur.execute(sql, (nome_usuarios, email, senha))

            # Salva as alterações no banco de dados
            conn.commit()

    except sqlite3.OperationalError as e:
        print("ERRO: ", e)

