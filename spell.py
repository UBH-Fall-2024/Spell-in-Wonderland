from flask import Blueprint, send_file, make_response
from pymongo import MongoClient
import boto3

spell_bp = Blueprint('spell_bp', __name__,
    template_folder='templates',
    static_folder='static')

@spell_bp.route('/spell', methods=["GET"])
def home():
    response = send_file('./templates/spell.html', mimetype='text/html')
    return make_response(response)

@spell_bp.route('/spellStyles.css', methods=["GET"])
def serve_home_css():
    response = send_file('./templates/spellStyles.css', mimetype='text/css')
    return make_response(response)