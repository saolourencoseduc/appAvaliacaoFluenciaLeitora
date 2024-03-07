# database.py

from flask import current_app
from app.extensions import db
from app.models.models import Avaliacao  # Assuming Avaliacao model is defined in your models.py

def insert_transcription_into_db(transcript, accuracy, word_count, wpm, duration, fluency_level, crdi, id_avaliacao):
    try:
        # Ensure id_avaliacao is correctly converted to int or handled if not provided/invalid
        id_avaliacao_int = int(id_avaliacao) if id_avaliacao.isdigit() else None
        
        new_aval = Avaliacao(
            transcription=transcript, 
            accuracy=accuracy, 
            word_count=word_count, 
            wpm=wpm, 
            audio_duration=duration, 
            aluno_leitura=fluency_level, 
            crdi=crdi, 
            id_avaliacao=id_avaliacao_int
        )
        db.session.add(new_aval)
        db.session.commit()
        return True  # Success
    except Exception as e:
        current_app.logger.error(f"Failed to insert transcription into database: {e}")
        db.session.rollback()
        return False  # Failure
