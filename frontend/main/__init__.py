import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    load_dotenv()

    app.config['APP_URL'] = os.getenv ['API_URL']
    app.config['SECRET_KEY'] = os.getenv ['SECRET_KEY']

    from main.routes import main
    app.register_blueprint(routes.main.main)
    
    return app