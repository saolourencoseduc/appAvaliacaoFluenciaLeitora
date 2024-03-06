from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class Avaliacao(db.Model):
    __tablename__ = 'Avaliacao'
    
    id = db.Column(db.Integer, primary_key=True)
    transcription = db.Column(db.Text, nullable=False)
    accuracy = db.Column(db.Float)
    word_count = db.Column(db.Integer)
    wpm = db.Column(db.Float)
    audio_duration = db.Column(db.Float)
    aluno_leitura = db.Column(db.Text)
    crdi = db.Column(db.Float)
    id_avaliacao = db.Column(db.Integer)
