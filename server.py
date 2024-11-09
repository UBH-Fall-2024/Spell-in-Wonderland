from flask import Flask, Blueprint
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongo")
db = client["Spell-in-Wonderland"]
word = db['word']



from home import home_bp
from spell import spell_bp

app.register_blueprint(home_bp)
app.register_blueprint(spell_bp)