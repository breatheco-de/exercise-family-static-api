"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

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
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

#AQUÍ AGREGA UN NUEVO MIEMBRO A LA FAMILIA
@app.route('/member', methods=["POST"])
def create_member():
    first_name = request.json.get("first_name")
    age = request.json.get("age")
    lucky_numbers = request.json.get("lucky_numbers")

    if not first_name or not isinstance(age, int) or not isinstance(lucky_numbers, list) or age <= 0:
        return jsonify({"error": "Invalid data provided"}), 400

    member = {
        "first_name": first_name,
        "age": age,
        "lucky_numbers": lucky_numbers,
        "last_name": jackson_family.last_name, 
        "id": jackson_family._generateId()
    }

    jackson_family.add_member(member)
    return jsonify(member), 200

# ElimiNA MIEMBRO X ID
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    success = jackson_family.delete_member(member_id)
    if success:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
