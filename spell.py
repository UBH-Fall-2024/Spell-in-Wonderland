from flask import Blueprint, send_file, make_response, request, render_template, current_app
from pymongo import MongoClient
import json
import boto3
import random

client = MongoClient("mongo")
db = client["Spell-in-Wonderland"]
words = db['word']
records = db['records']

spell_bp = Blueprint('spell_bp', __name__,
    template_folder='templates',
    static_folder='static')

@spell_bp.route('/white-rabbit-spell', methods=["GET"])
def easy_mode():
    response = send_file('./templates/spell.html', mimetype='text/html')
    if "user_id" not in request.cookies:
        return send_file('./templates/home.html', mimetype="text/html")
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.set_cookie("mode", value="easy", httponly=True, secure=True)
    return make_response(response)

@spell_bp.route('/cheshire-cat-spell', methods=["GET"])
def medium_mode():
    response = send_file('./templates/spell.html', mimetype='text/html')
    if "user_id" not in request.cookies:
        return send_file('./templates/home.html', mimetype="text/html")
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.set_cookie("mode", value="medium", httponly=True, secure=True)
    return make_response(response)

@spell_bp.route('/queen-of-hearts-spell', methods=["GET"])
def hard_mode():
    response = send_file('./templates/spell.html', mimetype='text/html')
    if "user_id" not in request.cookies:
        return send_file('./templates/home.html', mimetype="text/html")
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.set_cookie("mode", value="hard", httponly=True, secure=True)
    return make_response(response)

@spell_bp.route('/mad-hatter-spell', methods=["GET"])
def expert_mode():
    response = send_file('./templates/spell.html', mimetype='text/html')
    if "user_id" not in request.cookies:
        return send_file('./templates/home.html', mimetype="text/html")
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.set_cookie("mode", value="expert", httponly=True, secure=True)
    return make_response(response)

@spell_bp.route('/spell', methods=["GET"])
def get_word():
    needed_difficulty = request.cookies.get("mode")
    needed_user = request.cookies.get("user_id")
    chosen_word = choose_word(needed_difficulty, needed_user)
    data = {"word": chosen_word}
    return json.dumps(data)
    
@spell_bp.route('/spellStyles.css', methods=["GET"])
def serve_home_css():
    response = send_file('./templates/spellStyles.css', mimetype='text/css')
    response.headers["X-Content-Type-Options"] = "nosniff"
    return make_response(response)

def choose_word(mode:str, user_id:str):
    mode_words = list(words.find({"difficulty": mode}, {"word":1, "_id":0}))
    word_list = [word["word"] for word in mode_words]
    
    correct_word_list = records.find_one({"user_id": user_id}, {"correct":1, "_id":0})["correct"]

    result = list(filter(lambda x: x not in correct_word_list, word_list))
    return random.choice(result)