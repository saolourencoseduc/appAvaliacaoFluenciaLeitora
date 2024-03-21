from app.extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'

class Avaliacao(db.Model):
    __tablename__ = 'Avaliacao'
    id = db.Column(db.Integer, primary_key=True)
    transcription = db.Column(db.Text, nullable=True)  # Alterado para Text
    accuracy = db.Column(db.Float, nullable=True)
    word_count = db.Column(db.Integer, nullable=True)
    wpm = db.Column(db.Float, nullable=True)
    audio_duration = db.Column(db.Float, nullable=True)
    aluno_leitura = db.Column(db.String(255), nullable=True)  # Mantido como String, tamanho adequado
    crdi = db.Column(db.Float, nullable=True)
    id_avaliacao = db.Column(db.Integer, nullable=True)

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)  # Sem alteração necessária
    cpf = db.Column(db.String(14), nullable=True)  # Sem alteração necessária
    data_nascimento = db.Column(db.Date, nullable=True)  # Sem alterações necessárias
    escola = db.Column(db.String(120), nullable=True)  # Sem alteração necessária
    turma = db.Column(db.String(120), nullable=True)  # Sem alteração necessária
    serie = db.Column(db.String(120), nullable=True)  # Sem alteração necessária
    curso = db.Column(db.String(120), nullable=True)  # Sem alteração necessária
    ano = db.Column(db.Integer, nullable=False)  # Sem alterações necessárias
    turno = db.Column(db.String(120), nullable=True)  # Sem alteração necessária
    nome_mae = db.Column(db.String(120), nullable=True)  # Sem alteração necessária
    nome_pai = db.Column(db.String(120), nullable=True)  # Sem alteração necessária
    nome_responsavel = db.Column(db.String(120), nullable=True)  # Sem alteração necessária
