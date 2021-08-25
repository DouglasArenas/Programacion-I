import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    load_dotenv()

    from main.routes import main
    app.register_blueprint(routes.main.main)
    
    return app