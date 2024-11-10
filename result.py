from flask import Flask, Blueprint, send_file, render_template, make_response, request
from pymongo import MongoClient


client = MongoClient("mongo")
db = client["Spell-in-Wonderland"]
words = db['word']
records = db['records']

result_bp = Blueprint('result_bp', __name__,
    template_folder='templates',
    static_folder='static')

@result_bp.route('/result', methods=["GET"])
def result():
    response = send_file('./templates/result.html', mimetype='text/html')
    response = render_template('./templates/result.html')
    response.headers["X-Content-Type-Options"] = "nosniff"
    return make_response(response)

@result_bp.route('/result-api', methods=["GET"])
def result_api():
    user_id = request.cookies["user_id"]
    mode = request.cookies["mode"]

    mode_words = list(words.find({"difficulty": mode}, {"word":1, "_id":0}))
    word_list = [word["word"] for word in mode_words]

    correct_word_list = records.find_one({"user_id": user_id}, {"correct":1, "_id":0})["correct"]
    wrong_word_list = records.find_one({"user_id": user_id}, {"wrong":1, "_id":0})["wrong"]

    correct_word_list = list(filter(lambda x: x in correct_word_list, word_list))
    wrong_word_list = list(filter(lambda x: x in wrong_word_list, word_list))    

    return {
        "correct_word_list": correct_word_list,
        "wrong_word_list": wrong_word_list,
    }