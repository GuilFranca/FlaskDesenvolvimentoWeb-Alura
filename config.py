import os

SECRET_KEY = 'alura'

# Configuração da nossa aplicação
# Criando uma variável para a nossa aplicação
# URI (Identificador Uniforme de Recurso) é um padrão para identificar recursos na internet
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'Magnemite_EM1',
        servidor = 'localhost',
        database = 'jogoteca'
    )

# __file__ é uma forma de escrever uma referencia do porprio arquivo
# .dirname devolve o caminho do diretorio colocado dentro do mesmo
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'