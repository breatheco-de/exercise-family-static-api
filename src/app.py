
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

family = FamilyStructure("Jackson")

members = [
    {"id": 1, "first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]},
    {"id": 2, "first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]},
    {"id": 3, "first_name": "Jimmy", "age": 5, "lucky_numbers": [1]}
]

for member in members:
    member["last_name"] = family.last_name
    family.add_member(member)

@app.route('/')
def get_sitemap():
    endpoints = [str(rule) for rule in app.url_map.iter_rules()]
    return jsonify({"endpoints": endpoints}), 200

@app.route('/members', methods=['GET'])
def fetch_all_members():
    all_members = family.get_all_members()
    return jsonify(all_members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def fetch_member(member_id):
    member = family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"msg": "Member not found"}), 404

@app.route('/member', methods=['POST'])
def create_member():
    data = request.get_json()
    if "id" not in data:
        data["id"] = family._generateId()
    data["last_name"] = family.last_name
    family.add_member(data)
    return jsonify(data), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def remove_member(member_id):
    was_deleted = family.delete_member(member_id)
    if was_deleted:
        return jsonify({"done": True}), 200
    return jsonify({"msg": "Member not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)


