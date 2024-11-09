from flask import Blueprint, send_file, make_response
from pymongo import MongoClient

home_bp = Blueprint('home_bp', __name__,
    template_folder='templates',
    static_folder='static')

@home_bp.route('/home', methods=["GET"])
def home():
    response = send_file('./templates/home.html', mimetype='text/html')
    return make_response(response)

@home_bp.route('/templates/styles.css', methods=["GET"])
def serve_home_css():
    response = send_file('./templates/styles.css', mimetype='text/css')
    return make_response(response)
