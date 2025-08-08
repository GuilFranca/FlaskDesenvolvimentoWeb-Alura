from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instancia do Flask
app = Flask(__name__)
# Importando as configs para a aplicação
app.config.from_pyfile('config.py')

# Instancia banco de dados SQLAlchemy
# db = sqlalchemy(app)
db = SQLAlchemy(app)

# Importa tudo dentro do nosso arquivo views
from views import *

# app.run(debug=True)

# Está forma de inicializar a aplicação serve para rodar com todas essas importações que estamos fazendo
if __name__ == "__main__":
   app.run(debug=True)
