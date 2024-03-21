import logging
from flask import Flask, jsonify, current_app
from flask_login import LoginManager
from config import Config
from app.extensions import db
from app.api.routes import bp as api_bp
from app.models.models import User

# Cria uma instância do LoginManager
login_manager = LoginManager()
# Define a view de login para redirecionar usuários não autenticados.
login_manager.login_view = 'api.login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Definindo a SECRET_KEY
    app.config['SECRET_KEY'] = 'testefap123'

    db.init_app(app)

    if not app.debug:
        # Aqui está a linha corrigida
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        app.logger.addHandler(handler)

    # Registra o blueprint da API
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.errorhandler(Exception)
    def handle_exception(e):
        current_app.logger.error(f"Unhandled exception: {e}")
        response = jsonify({'error': 'Internal Server Error', 'details': str(e)})
        response.status_code = 500
        return response

    with app.app_context():
        db.create_all()

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
