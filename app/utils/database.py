# database.py

from flask import current_app, jsonify
from app.extensions import db
from app.models.models import Avaliacao  # Make sure to have an Avaliacao model defined in your models.py

def insert_transcription_into_db(transcript, accuracy, word_count, wpm, duration, fluency_level, crdi, id_avaliacao):
    try:
        new_aval = Avaliacao(
            transcription=transcript, 
            accuracy=accuracy, 
            word_count=word_count, 
            wpm=wpm, 
            audio_duration=duration, 
            aluno_leitura=fluency_level, 
            crdi=crdi, 
            id_avaliacao=id_avaliacao
        )
        db.session.add(new_aval)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(f"Failed to insert transcription into database: {e}")
        # Roll back the session in case of error
        db.session.rollback()
        response = jsonify({'error': 'Database operation failed', 'details': str(e)})
        response.status_code = 500
        return response
