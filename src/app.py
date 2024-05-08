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

#Get all members
@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

#Get one member
@app.route('/member/<int:id>', methods=['GET'])
def get_one_member(id):
    member = jackson_family.get_member(id)
    if member is None:
        return jsonify({"message": "member not found"}), 400
    return(member), 200

#post member
@app.route('/member', methods=['POST'])
def post_member():
    body = request.json
    new_members = jackson_family.add_member(body)
    return jsonify(new_members), 200

#delete member
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_members(id):
    member_deleted = jackson_family.delete_member(id)
    if member_deleted is not None:
        return jsonify({
        "done" : True
        })
    return jsonify({"message":"member not found"}), 400


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
