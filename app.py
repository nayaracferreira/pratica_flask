from flask import Flask
from db import database
app = Flask(__name__)
 
#  Para expor o resultado utilizamos a função @
@app.route("/")
def hello():
   return "Oi Flask!"

# Dicionário
@app.route("/data")
def pares():
   return {"nome": "Nayara"}

#Flask também aceita argumentos, especificando que tipo de dado eu quero
@app.route("/cumprimentar/<string:nome>")
#Agora ao cumprimentar uma pessoa eu quero adicionar o nome dela em um banco de dados(que é uma lista no arquivo criado db.py)
def cumprimentar(nome):
   database.append(nome)
   return f"Olá, {nome}"

#Rota de listagem
@app.route("/listar")
def listar():
   return "\n".join(database)

if __name__ == "__main__":
   app.run(debug=True)