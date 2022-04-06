# "Flask is one of the most popular web development frameworks for Python"
# Para rodar o flask, é necessário criar uma environment variable no cmd na pasta do arquivo.
# set FLASK_APP=nomedoprograma.py
from flask import Flask

app = Flask(__name__)
print(__name__)


# Quando o usuário vai para o endereço ("endereço"), o que está na função é executado.
# Esse @ é chamado de Python Decorator. Isso é: adicionar funcionalidades às funções que já existem.
@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def say_bye():
    return "Bye"


# Essa linha tira a necessidade de rodar o programa através do cmd
if __name__ == "__main__":
    app.run()
