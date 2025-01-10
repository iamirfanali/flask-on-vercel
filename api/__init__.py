from flask import Flask
from .routes import register_blueprints
from .middlewares import setup_middlewares

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    register_blueprints(app)

    # Setup Middlewares
    setup_middlewares(app)

    return app
