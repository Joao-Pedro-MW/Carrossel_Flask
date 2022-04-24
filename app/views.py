from app import app
from flask import render_template 
"""importamos a biblioteca que renderiza
nosso arquivo html usando o Jinja"""
@app.route("/")
def index(): #renderiza a página index.html como pagina padrão/index
    return render_template("index.html")