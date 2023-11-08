from flask import Flask 
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    