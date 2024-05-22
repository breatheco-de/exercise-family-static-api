"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from datastructures import Family
from utils import APIException, generate_sitemap

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Crear la instancia de la familia Jackson
jackson_family = Family("Jackson")

# Manejar/serializar errores como un objeto JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generar sitemap con todos tus endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(response_body), 200

@app.route('/member', methods=['POST'])
def add_a_member():
    body = request.get_json()

    first_name = body["first_name"]
    age = body["age"]
    lucky_numbers = body["lucky_numbers"]

    member = {
        "first_name": first_name,
        "age": age,
        "lucky_numbers": lucky_numbers,
    }

    jackson_family.add_member(member)

    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }

    return jsonify(response_body), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({'error': 'Member not found'}), 400

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    success = jackson_family.delete_member(member_id)
    if success:
        return jsonify({'done': True}), 200
    else:
        return jsonify({'error': 'Failed to delete member'}), 400

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)