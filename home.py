from flask import Blueprint, send_file, make_response
from pymongo import MongoClient
import csv
import random

client = MongoClient("mongo")
db = client["Spell-in-Wonderland"]
word = db['word']

home_bp = Blueprint('home_bp', __name__,
    template_folder='templates',
    static_folder='static')

def csv_to_db():
    word.remove({})
    ids = []
    with open('words.csv', 'r') as words:
        reader = csv.DictReader(words, fieldnames=None)
        for row in reader:
            print(row)
            id = random.randint(0, 200)
            if id not in ids:
                word.insert_one({'id': id, 'word':row['Word'], 'difficulty':row['Difficulty']})

@home_bp.route('/home', methods=["GET"])
def home():
    response = send_file('./templates/home.html', mimetype='text/html')
    csv_to_db()
    return make_response(response)

@home_bp.route('/styles.css', methods=["GET"])
def serve_home_css():
    response = send_file('./templates/styles.css', mimetype='text/css')
    return make_response(response)
