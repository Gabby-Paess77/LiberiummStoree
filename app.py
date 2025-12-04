from flask import Flask, render_template, url_for, request, redirect, session, send_file, Response, jsonify
import sqlite3
import io

app = Flask(__name__)
app.secret_key = "chave_secreta"


# ---------------- FUNÇÃO DE CONEXÃO ----------------
def conectar_banco():
    return sqlite3.connect("LiberiumStore.db")


# ---------------- PÁGINAS PRINCIPAIS ----------------
@app.route('/')
def index():
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT nome_leitor,
             comentario_leitor 
            FROM comentario 
            ORDER BY comentario_id DESC
        """)
        comentarios = cursor.fetchall()
    return render_template('index.html',
                           comentarios=comentarios)


@app.route('/leitor')
def leitor():
    return render_template('leitor.html')


@app.route('/escritores')
def escritores():
    return render_template('escritores.html')


# ---------------- PÁGINAS DO ESCRITOR ----------------
@app.route('/sobreescritores')
def sobreescritores():
    return render_template('sobreescritores.html')


@app.route('/contatoescritor')
def contatoescritor():
    return render_template('contatoescritor.html')


@app.route('/livrosescritores')
def livrosescritores():
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT livro_id, titulo_livro, preco_livro, 
            escritor, 
            descricao_livro, 
            capa_livro
            FROM livros
            ORDER BY livro_id DESC
        """)
        livros = cursor.fetchall()
    return render_template('livrosescritores.html',
                           livros=livros)




# ---------------- LIVRO ESPECÍFICO ----------------
@app.route('/livro/<int:livro_id>', methods=['GET', 'POST'])
def livro_especifico(livro_id):
    with conectar_banco() as conexao:
        cursor = conexao.cursor()

        if request.method == 'POST':
            nome = request.form.get('nomeLivro')
            preco = request.form.get('preco')
            autor = request.form.get('nomeAutor')
            descricao = request.form.get('descricao')
            pdf = request.files.get('pdfLivro')
            capa = request.files.get('capaLivro')

            if pdf and pdf.filename:
                cursor.execute("UPDATE livros SET pdf_livro = ? WHERE livro_id = ?",
                               (pdf.read(), livro_id))

            if capa and capa.filename:
                cursor.execute("UPDATE livros SET capa_livro = ? WHERE livro_id = ?",
                               (capa.read(), livro_id))

            cursor.execute("""
                UPDATE livros
                SET titulo_livro = ?, escritor = ?, preco_livro = ?, descricao_livro = ?
                WHERE livro_id = ?
            """, (nome, autor, preco, descricao, livro_id))

            conexao.commit()
            return redirect(url_for('livro_especifico', livro_id=livro_id))

        cursor.execute("""
            SELECT livro_id, titulo_livro, escritor, preco_livro, descricao_livro, capa_livro, pdf_livro
            FROM livros
            WHERE livro_id = ?
        """, (livro_id,))
        livro = cursor.fetchone()

    if not livro:
        return "Livro não encontrado", 404

    return render_template('livroespecifico.html', livro=livro)

# ---------------- COMPRAR O LIVRO  ----------------


@app.route("/comprar", methods=["POST"])
def comprar():
    data = request.get_json()
    leitor_id = data.get("leitor_id")
    livro_id = data.get("livro_id")
    metodo_pago = data.get("metodo_pago")
    valor_pago = data.get("valor_pago")

    try:
        conn = sqlite3.connect("seu_banco.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO pagamento (leitor, livro_id, metodo_pago, valor_pago, data_pago)
            VALUES (?, ?, ?, ?, ?)
        """, (leitor_id, livro_id, metodo_pago, valor_pago, date.today()))
        conn.commit()
        conn.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


# ---------------- MINHA CONTA / TODOS OS LIVROS ----------------
@app.route('/minhaconta')
def minhaconta_view():
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT livro_id, titulo_livro, preco_livro, escritor,
             descricao_livro, capa_livro, pdf_livro
            FROM livros
            ORDER BY livro_id DESC
        """)
        livros = cursor.fetchall()

    return render_template('minhaconta.html', livros=livros)


# ---------------- CADASTRAR LIVRO ----------------
@app.route('/cadastrar_livro', methods=['POST'])
def cadastrar_livro():

    nome = request.form.get('nomeLivro')
    escritor = request.form.get('nomeAutor')
    preco = request.form.get('preco')
    descricao = request.form.get('descricao')
    pdf = request.files.get('pdfLivro')
    capa = request.files.get('capaLivro')

    if not (nome and escritor and preco and descricao):
        return "Preencha todos os campos!", 400

    pdf_bytes = pdf.read() if pdf else None
    capa_bytes = capa.read() if capa else None

    try:
        conn = conectar_banco()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO livros (titulo_livro, escritor, preco_livro, descricao_livro, pdf_livro, capa_livro)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, escritor, preco, descricao, pdf_bytes, capa_bytes))

        conn.commit()

    except Exception as e:
        print("Erro ao cadastrar livro:", e)
        return f"Erro: {e}", 500

    finally:
        conn.close()

    return redirect(url_for('minhaconta_view'))






@app.route('/editar_livro/<int:id>', methods=['POST'])
def editar_livro(id):
    nome = request.form.get('nomeLivro')
    preco = request.form.get('preco')
    autor = request.form.get('nomeAutor')
    descricao = request.form.get('descricao')

    pdf = request.files.get('pdfLivro')
    capa = request.files.get('capaLivro')

    with conectar_banco() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE livros
            SET titulo_livro = ?, escritor = ?, preco_livro = ?, descricao_livro = ?
            WHERE livro_id = ?
        """, (nome, autor, preco, descricao, id))

        if pdf and pdf.filename:
            cursor.execute("UPDATE livros SET pdf_livro = ? WHERE livro_id = ?", (pdf.read(), id))

        if capa and capa.filename:
            cursor.execute("UPDATE livros SET capa_livro = ? WHERE livro_id = ?", (capa.read(), id))

        conn.commit()

    return redirect(url_for('livro_especifico', livro_id=id))


@app.route('/excluir_livro/<int:id>', methods=['POST'])
def excluir_livro(id):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM livros WHERE livro_id = ?",
                       (id,))
        conn.commit()

    return redirect(url_for('minhaconta_view'))



# ---------------- CAPA E PDF ----------------
@app.route('/capa_livro/<int:livro_id>')
def capa_livro(livro_id):
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT capa_livro FROM livros WHERE livro_id = ?",
                       (livro_id,))
        capa = cursor.fetchone()

    if capa and capa[0]:
        return Response(capa[0], mimetype="image/jpeg")

    return Response(open("static/IMAGENS/LIVROS/semcapa.png", "rb").read(),
                    mimetype="image/png")


@app.route('/pdf_livro/<int:livro_id>')
def pdf_livro(livro_id):
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT pdf_livro FROM livros WHERE livro_id = ?",
                       (livro_id,))
        pdf = cursor.fetchone()

    if pdf and pdf[0]:
        return send_file(io.BytesIO(pdf[0]), mimetype='application/pdf')

    return "PDF não encontrado", 404


# ---------------- LEITOR / CONTATOS / COMENTÁRIOS ----------------
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/contatoleitor')
def contatoleitor():
    return render_template('contatoleitor.html')


@app.route('/livrosleitor')
def livrosleitor():
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT livro_id, titulo_livro, preco_livro,
             escritor, descricao_livro, capa_livro
            FROM livros
            ORDER BY livro_id DESC
        """)
        livros = cursor.fetchall()
    return render_template('livrosleitor.html',
                           livros=livros)


@app.route('/salvar_comentario', methods=['POST'])
def salvar_comentario():
    nome_leitor = request.form.get('nome_leitor')
    comentario_leitor = request.form.get('comentario_leitor')

    if nome_leitor and comentario_leitor:
        with conectar_banco() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO comentario (nome_leitor,
                 comentario_leitor)
                VALUES (?, ?)
            """, (nome_leitor, comentario_leitor))
            conexao.commit()

    return redirect(url_for('leitor'))


@app.route('/salvar_contato', methods=['POST'])
def salvar_contato():
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO contato_leitor (email, nome, senha, telefone, mensagem)
            VALUES (?, ?, ?, ?, ?)
        """, (
            request.form['email'],
            request.form['nome'],
            request.form['senha'],
            request.form['telefone'],
            request.form['mensagem']
        ))
        conexao.commit()
    return redirect(url_for('contatoleitor'))


@app.route('/salvar_contato_escritor', methods=['POST'])
def salvar_contato_escritor():
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO contato_escritor (email, 
            nome, senha, telefone, mensagem)
            VALUES (?, ?, ?, ?, ?)
        """, (
            request.form['email'],
            request.form['nome'],
            request.form['senha'],
            request.form['telefone'],
            request.form['mensagem']
        ))
        conexao.commit()
    return redirect(url_for('contatoescritor'))









# ---------------- EXECUÇÃO ----------------
if __name__ == '__main__':
    app.run(debug=True)
