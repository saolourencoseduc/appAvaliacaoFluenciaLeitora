from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required
from app.extensions import db
from app.models.models import Aluno, User
from ..services.transcription_service import process_audio_and_transcribe

bp = Blueprint('api', __name__)

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()

    # Verifique se o usuário existe e se a senha está correta
    if user and check_password_hash(user.password_hash, password):
        login_user(user, remember=True)  # Inicia a sessão para o usuário
        return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@bp.route('/logout')
@login_required  # Garante que apenas usuários autenticados possam fazer logout
def logout():
    logout_user()  # Encerra a sessão do usuário
    return jsonify({'message': 'Logged out successfully'}), 200

@bp.route('/users', methods=['GET'])
@login_required  # Garante que apenas usuários autenticados possam acessar a lista de usuários
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

@bp.route('/transcribe', methods=['POST'])
@login_required  # Você pode querer restringir esta rota a usuários autenticados
def transcribe_audio_api():
    response, status_code = process_audio_and_transcribe(request)
    return response, status_code

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

@bp.route('/alunos', methods=['GET'])
@login_required  # Se desejar restringir esta rota a usuários autenticados
def list_alunos():
    alunos = Aluno.query.all()
    return jsonify([{'id': aluno.id, 'nome': aluno.nome, 'cpf': aluno.cpf} for aluno in alunos])
