"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the Jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    response.headers['Content-Type'] = 'application/json'
    return response

# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    response = make_response(generate_sitemap(app))
    response.headers['Content-Type'] = 'application/json'  # Maintain 'application/json'
    return response

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    response = {
        "family": members
    }
    return jsonify(response), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if not member:
        return jsonify({"error": "Member not found"}), 404

    return jsonify(member), 200

@app.route('/member', methods=['POST'])
def add_member():
    member_data = request.get_json()
    if not member_data or "first_name" not in member_data or "age" not in member_data:
        return jsonify({"error": "Invalid data. 'first_name' and 'age' are required."}), 400

    jackson_family.add_member(member_data)
    return jsonify({"message": "Member added successfully"}), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    result = jackson_family.delete_member(member_id)
    if not result:
        return jsonify({"error": "Member not found"}), 404

    return jsonify({"message": "Member deleted successfully"}), 200

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
