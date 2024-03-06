# app/__init__.py

from flask import Flask, jsonify, current_app
from config import Config
from app.api.routes import bp as api_bp
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)  # Bind SQLAlchemy to the Flask app

    # Set up logging
    if not app.debug:
        import logging
        from logging import StreamHandler
        handler = StreamHandler()
        handler.setLevel(logging.INFO)
        app.logger.addHandler(handler)

    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')

    # Custom error handler
    @app.errorhandler(Exception)
    def handle_exception(e):
        current_app.logger.error(f"Unhandled exception: {e}")
        response = jsonify({'error': 'Internal Server Error', 'details': str(e)})
        response.status_code = 500
        return response

    # Import models here to ensure they are known to SQLAlchemy
    with app.app_context():
        from app.models import models
        db.create_all()

    return app
