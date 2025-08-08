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