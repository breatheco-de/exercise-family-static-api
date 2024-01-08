"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    members = jackson_family.get_all_members()
    response_body = {"members": members}
    return jsonify(response_body), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404

    response_body = {
        "id": member['id'],
        "first_name": member["first_name"],
        "age": member["age"],
        "lucky_numbers": member["lucky_numbers"]
    }

    return jsonify(response_body), 200


@app.route('/member', methods=['POST'])
def add_member():

    request_body = request.get_json(force=True)
    if "first_name" not in request_body:
        return jsonify("The first name is requeried"), 401

    if "age" not in request_body:
        return jsonify("The age is requeired"), 401

    if "lucky_numbers" not in request_body:
        return jsonify("The lucky numbers are requeired"), 401

    id = jackson_family._generateId()

    if "id" in request_body:
        id = request_body['id']

    member = {
        "id": id,
        "first_name": request_body['first_name'],
        "age": request_body['age'],
        "lucky_numbers": request_body['lucky_numbers']
    }

    response_body = {
        "msg": "Member add success",
        "Member": member
    }

    jackson_family.add_member(member)

    return jsonify(response_body), 200


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    jackson_family.delete_member(member_id)

    return jsonify({"done": True}), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)