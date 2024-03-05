# app/api/routes.py
from flask import Blueprint, request, jsonify

from app.models.models import User
from ..services.transcription_service import process_audio_and_transcribe

bp = Blueprint('api', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

@bp.route('/transcribe', methods=['POST'])
def transcribe_audio_api():
    # Adjusted to use process_audio_and_transcribe directly
    response, status_code = process_audio_and_transcribe(request)
    return response, status_code


# Root route providing API information
@bp.route('/')
def index():
    return jsonify({
        'message': 'Welcome to the Fluency Assesment API',
        'usage': {
            'transcribe_audio': {
                'method': 'POST',
                'endpoint': '/transcribe',
                'description': 'Submit an audio file for transcription.',
                'required_fields': ['audio_file', 'reference_text', 'id_avaliacao'],
            }
        },
        'note': 'Please refer to the API documentation for more details.'
    })