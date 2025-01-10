from flask import Flask
from .process_data import process_data_bp

def register_blueprints(app: Flask):
    app.register_blueprint(process_data_bp, url_prefix="/api")
