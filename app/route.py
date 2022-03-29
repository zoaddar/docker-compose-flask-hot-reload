from flask import Flask 
import requests

from config.config import Config
from config.database import Database

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!! '

@app.route('/db')
def db():
    return Database.mysql


if __name__ == '__main__':
    app.run(debug = Config.debug, host = '0.0.0.0')