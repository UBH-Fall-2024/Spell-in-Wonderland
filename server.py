from flask import Flask, Blueprint
from pymongo import MongoClient
import csv

app = Flask(__name__)

client = MongoClient("mongo")
db = client["Spell-in-Wonderland"]
word = db['word']

from home import home_bp
from spell import spell_bp

app.register_blueprint(home_bp)
app.register_blueprint(spell_bp)

def csv_to_db():
    reader = csv.DictReader(open('word.csv'))
    for row in reader:
        word.insert_one({'difficulty':row[0]})
        word.insert_one({'word':row[1]})