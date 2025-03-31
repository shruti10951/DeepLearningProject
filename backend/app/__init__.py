from flask import Flask
from flask_cors import CORS

from .routes.predict import predict_bp
from .routes.denoise import denoise_bp 

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})  # Allow frontend origin

    # Register blueprints
    app.register_blueprint(predict_bp, url_prefix='/model')
    app.register_blueprint(denoise_bp, url_prefix="/model")  # Add denoise route

    return app
