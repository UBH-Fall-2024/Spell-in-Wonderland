from flask import Blueprint
from pymongo import MongoClient
import boto3

spell_bp = Blueprint('spell_bp', __name__,
    template_folder='templates',
    static_folder='static')

@spell_bp.route('/baz.bar')
def foo():
    pass
