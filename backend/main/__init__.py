import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.recursos as recursos

api = Api()

def create_app():
    app = Flask(name)
    load_dotenv()
    api.add_recursos()
    api.add_recursos()
    api.init__app(app)
    return app
