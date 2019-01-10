from flask import Flask, Blueprint, jsonify, make_response
from ..models.questions import *

question_api = Blueprint('questions_api', __name__, )

questionmodel = Questions()


@question_api.route('/questions/', methods=["GET"])
def get_questions():
    questions_list = questionmodel.get_questions()
    return make_response(jsonify({"message": questions_list}), 200)


@question_api.route('/questions/<string:id>', methods=["GET"])
def get_question(id):
    single_question = questionmodel.get_question(id)
    return make_response(jsonify({"message": single_question}), 200)


@question_api.route('/questions/post', methods=["POST"])
def question_post():
    return make_response(jsonify({"message": "post a question"}), 201)


@question_api.route('/questions/<string:id>/upvote', methods=["PATCH"])
def upvote(id):
    return make_response(jsonify({"message": "upvote"}), 204)


@question_api.route('/questions/<string:id>/downvote', methods=["PATCH"])
def downvote(id):
    return make_response(jsonify({"message": " downvote "}), 204)
