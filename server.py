from flask import Flask, Blueprint
from pymongo import MongoClient
import csv
import random

app = Flask(__name__, static_url_path='/static')

client = MongoClient("mongo")
db = client["Spell-in-Wonderland"]
words = db['words']
records = db['records']

from home import home_bp
from spell import spell_bp
from result import result_bp

app.register_blueprint(home_bp)
app.register_blueprint(spell_bp)
app.register_blueprint(result_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

