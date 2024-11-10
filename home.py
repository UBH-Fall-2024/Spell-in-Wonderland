from flask import Blueprint, send_file, make_response, request
from pymongo import MongoClient
import secrets
import csv
import random

client = MongoClient("mongo")
db = client["Spell-in-Wonderland"]
words = db['word']
records = db['records']

home_bp = Blueprint('home_bp', __name__,
    template_folder='templates',
    static_folder='static')

def csv_to_db():
    words.remove({})
    ids = []
    with open('words.csv', 'r') as readIN:
        reader = csv.DictReader(readIN, fieldnames=None)
        for row in reader:
            id = random.randint(0, 200)
            if id not in ids:
                words.insert_one({'id': id, 'word':row['Word'], 'difficulty':row['Difficulty']})

@home_bp.route('/')
@home_bp.route('/home', methods=["GET"])
def home():
    response = send_file('./templates/home.html', mimetype='text/html')
    if 'user_id' not in request.cookies:
        response.set_cookie("user_id", value=add_user(secrets.token_urlsafe(80)), httponly=True) #secure=True)
    response.headers["X-Content-Type-Options"] = "nosniff"
    csv_to_db()
    return make_response(response)

@home_bp.route('/styles.css', methods=["GET"])
def serve_home_css():
    response = send_file('./templates/styles.css', mimetype='text/css')
    response.headers["X-Content-Type-Options"] = "nosniff"
    return make_response(response)

def add_user(user_id:str):
    user = {"user_id": user_id,
            "correct": [],
            "incorrect": []}
    records.insert_one(user)
    return user_id

