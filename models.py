from jogoteca import db

# Classe model ponte com banco de dados Jogos
class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    # Função repr
    def __repr__(self):
        return '<Name %r>' % self.nome


# Classe model ponte com banco de dados Usuarios
class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    # Função repr
    def __repr__(self):
        return '<Name %r>' % self.nome