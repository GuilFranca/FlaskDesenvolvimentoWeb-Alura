from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app, db
from models import Jogos, Usuarios

@app.route("/")
def index():
    # Jogos representa uma tabela do banco de dados, cada objeto dessa class é uma linha na tabela
    # .query é um método que inicia uma consulta ao banco de dados
    # .order_by(Jogos.id) é um método que organiza a ordem dos resultados pelo id dos jogos
    # O resultado desta consulta é uma lista de jogos
    listaJogos = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo='Jogos', jogos=listaJogos)


@app.route("/novo")
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route("/criar", methods=['GET', 'POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    # Realiza a verificação se já existe um jogo com o nome inserido
    jogo = Jogos.query.filter_by(nome = nome).first()

    # Se já houver um jogo com este nome, será exibido uma mensagem avisando isso e a página será redirecionada para a página index
    if jogo:
        flash('Jogo já existente!')
        return redirect(url_for('index'))
    
    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    # instanciação do SQLAlchemy adicionar o novo jogo
    db.session.add(novo_jogo)
    # Commita no banco de dados
    db.session.commit()
    
    # Redireciona para a página em questão
    # Com url_for passamos a função que instância a página em questão
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)


@app.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    # Usuarios representa a tabela usuários
    # será realizada uma query utlizando um filtro de nickname
    # Caso exista um nickname do mesmo a variável usuario sera True, caso contrário a variável será False
    # a variável usuario recebera a consulta com o nickname pesquisado virando o objeto desse usuário
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            # Mensagem de logado com sucesso
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

# for jogo in listaJogos:
#     print(jogo.nome)