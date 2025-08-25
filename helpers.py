import os
from jogoteca import app

def recupera_imagem(id):
    # Navega por todas as capas dentro da pasta uploads e verifica se a mesa possui o mesmo id do jogo que queremos, caso não tenha devolve a capa padrão
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}.jpg' == nome_arquivo:
            return nome_arquivo
    
    return 'capa_padrao.jpg'
