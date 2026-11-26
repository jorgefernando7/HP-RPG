from flask import Flask, render_template, request, redirect, url_for
import sqlite3

from regras_ordem import classes, origens

app = Flask(__name__)

#BANCO DE DADOS

def conectar_banco():
    return sqlite3.connect("hp_rpg.db")

def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()

criar_tabela()

#ROTAS DAS PÁGINAS

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        nome = request.form["nome"]
        senha = request.form["senha"]

        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM usuarios WHERE nome = ? AND senha = ?",
            (nome, senha)
        )

        usuario = cursor.fetchone()

        conexao.close()

        if usuario:
            return redirect(url_for("menu"))

        return "Nome ou senha incorretos!"

    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/personagens")
def personagens():
    return render_template("personagens.html")

@app.route("/escolher_sistema")
def escolher_sistema():
    return render_template("escolher_sistema.html")

@app.route("/criar/ordem", methods=["GET", "POST"])
def criar_ordem():

    return render_template(
        "criar_ordem.html",
        classes=classes,
        origens=origens
    )

@app.route("/criar/2d6")
def criar_2d6():
    return "Aqui ficará a ficha 2D6"

@app.route("/campanhas")
def campanhas():
    return render_template("campanhas.html")

@app.route("/criar_personagem")
def criar_personagem():
    return render_template("criar_personagem.html")

@app.route("/meus_personagens")
def meus_personagens():
    return render_template("meus_personagens.html")

#CADASTRO DE USUARIO

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO usuarios (nome, email, senha)
            VALUES (?, ?, ?)
        """, (nome, email, senha))

        conexao.commit()
        conexao.close()

        return "Cadastro realizado com sucesso!"

    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)