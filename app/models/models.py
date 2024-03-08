from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)  # made nullable
    email = db.Column(db.String(120), unique=True, nullable=True)  # made nullable

    def __repr__(self):
        return f'<User {self.username}>'

class Avaliacao(db.Model):
    __tablename__ = 'Avaliacao'
    
    id = db.Column(db.Integer, primary_key=True)
    transcription = db.Column(db.Text, nullable=True)  # made nullable
    accuracy = db.Column(db.Float, nullable=True)
    word_count = db.Column(db.Integer, nullable=True)
    wpm = db.Column(db.Float, nullable=True)
    audio_duration = db.Column(db.Float, nullable=True)
    aluno_leitura = db.Column(db.Text, nullable=True)
    crdi = db.Column(db.Float, nullable=True)
    id_avaliacao = db.Column(db.Integer, nullable=True)

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(14), nullable=True)
    data_nascimento = db.Column(db.Date, nullable=True)
    escola = db.Column(db.String(120), nullable=True)
    turma = db.Column(db.String(120), nullable=True)
    serie = db.Column(db.String(120), nullable=True)
    curso = db.Column(db.String(120), nullable=True)
    ano = db.Column(db.Integer, nullable=False)
    turno = db.Column(db.String(120), nullable=True)
    nome_mae = db.Column(db.String(120), nullable=True)
    nome_pai = db.Column(db.String(120), nullable=True)
    nome_responsavel = db.Column(db.String(120), nullable=True)
