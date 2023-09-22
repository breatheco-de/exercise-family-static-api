"""
This module takes care of starting the API Server, Loading the DB, and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members)


@app.route('/member', methods=['POST'])
def handle_add_member():
    new_member = request.get_json(force=True)
    jackson_family.add_member(new_member)

    return jsonify({"message": "New family member added!"}), 200

@app.route('/member/<int:id>', methods=['GET'])
def handle_get_member(id):
    member = jackson_family.get_member(id)
    if member is not None:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Family member not found"}), 404

@app.route('/member/<int:id>', methods=['DELETE'])
def handle_delete_member(id):
    member = jackson_family.get_member(id)
    if member is not None:
        jackson_family.delete_member(id)
        return jsonify({"message": f"Family member {member['first_name']} was deleted"}), 200
    else:
        return jsonify({"error": "Family member not found"}), 404

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
