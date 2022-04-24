from flask import Flask
#importa o flask 
#sem o arquivo __init__ nosso programa não funciona, pois ele quem é nosso construtor
#pois ele que mostra ao Flask onde "seguir"
app = Flask(__name__)#define nosso arqquivo como programa
from app import views