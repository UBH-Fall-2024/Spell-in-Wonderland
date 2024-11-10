from flask import Blueprint, send_file, make_response, request
from pymongo import MongoClient
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
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.set_cookie("mode", value="easy", httponly=True, secure=True)
    return make_response(response)

@spell_bp.route('/cheshire-cat-spell', methods=["GET"])
def medium_mode():
    response = send_file('./templates/spell.html', mimetype='text/html')
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.set_cookie("mode", value="medium", httponly=True, secure=True)
    return make_response(response)

@spell_bp.route('/queen-of-hearts-spell', methods=["GET"])
def hard_mode():
    response = send_file('./templates/spell.html', mimetype='text/html')
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.set_cookie("mode", value="hard", httponly=True, secure=True)
    return make_response(response)

@spell_bp.route('/mad-hatter-spell', methods=["GET"])
def expert_mode():
    response = send_file('./templates/spell.html', mimetype='text/html')
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.set_cookie("mode", value="expert", httponly=True, secure=True)
    return make_response(response)

@spell_bp.route('/spellStyles.css', methods=["GET"])
def serve_home_css():
    response = send_file('./templates/spellStyles.css', mimetype='text/css')
    response.headers["X-Content-Type-Options"] = "nosniff"
    return make_response(response)