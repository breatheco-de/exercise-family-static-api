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
pets_family = FamilyStructure("Pets")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET', 'POST'])
def handle_members():

    if request.method == "GET":
        members = pets_family.get_all_members()
        response_body = {
            "pets-family":members
        }
        return jsonify(response_body), 200
    
    elif request.method == "POST":
        try:
            new_member_data = request.json

            print("ESTO ES REQUEST ->",request.json)
            for member in new_member_data:
                pets_family.add_member(member)


            return jsonify(new_member_data), 201
        
        except Exception as e:
            raise APIException(str(e), status_code=400)


    return jsonify(response_body), 200



@app.route('/members/<int:member_id>', methods=["DELETE", "PUT", "GET"])
def handle_delete_member(member_id):

    if request.method == "PUT":
        try:
            updated_data = request.json
            updated_member = pets_family.update_member(member_id, updated_data)
            return jsonify(updated_member), 200
        
        except ValueError as ve:
            raise APIException(str(ve), status_code=404)
        
    elif request.method == "GET":
        try:
            get_member = pets_family.get_member(member_id)
            return jsonify(get_member), 200
        
        except ValueError as ve:
            raise APIException(str(ve), status_code=404)


    elif request.method == "DELETE":

        try:
            deleted_member = pets_family.delete_member(member_id)
            return jsonify(deleted_member), 200
        
        except ValueError as ve:
            raise APIException(str(ve), status_code=404)







# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
