from flask import Flask,Blueprint,jsonify,make_response, request
from ..models.meetups import *

meetup_api = Blueprint('meetup_api',__name__,)
meetupmodel = Meetups_Model

"""Get all meetups"""
@meetup_api.route('/meetups/',methods=["GET"])
def get_meetups():

    meetups_list = meetupmodel().get_meetups()
    return make_response(jsonify({"Meetup_list": meetups_list}),200)


"""Get single meetup"""
@meetup_api.route('/meetups/<string:id>',methods=["GET"])
def get_meetup(id):
    meetup_details = meetupmodel().get_meetup()
    return make_response(jsonify({"single meetup ":meetup_details}),200)


"""RSVP a single meetup"""
@meetup_api.route('/meetups/<string:id>/rsvps',methods=["POST"])
def handle_meetup_rsvp(id):

    data = request.get_json()
    username = data['name']
    meetup_id= id
    status = data['status']


    if username == "" or meetup_id == "" or status == "":
        return make_response(jsonify({"message":"Error! missing vital data"}))

    """TODO"""
    """Add method to handle RSVP. """
    return make_response(jsonify({"rsvp " : data}),201)