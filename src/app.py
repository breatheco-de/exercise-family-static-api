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
def get_all_member():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member', methods=['POST'])
def add_member():
    member_data = request.get_json()
    if not member_data or "first_name" not in member_data:
        raise APIException("You must specify the member's first name", status_code=400)
    jackson_family.add_member(member_data)
    return jsonify({"message": "Member added succesfully"}), 200

@app.route('/member/<int:id>', methods=['DELETE'])
def deleter_member(id):
    member = jackson_family.get_member(id)
    if not member:
        raise APIException("Member not found", status_code=404)
    
    jackson_family.delete_member(id)
    return jsonify({"message": "Member deleted sucessfully"}), 200

@app.route('/member/<int:id>', methods=['PUT'])
def update_member(id):
    member_data = request.get_json()
    member = jackson_family.get_member(id)
    if not member:
        raise APIException("Member not found", status_code=404)
    
    jackson_family.update_member(id, member_data)
    return jsonify({"message": "Member updated successfully"}), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    if not member:
        raise APIException("Member not found", status_code=404)
    
    return jsonify(member), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
