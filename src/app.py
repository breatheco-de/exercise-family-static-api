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
jackson_family = FamilyStructure("Jackson")  # Create the jackson family object


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


"""
CRUD
'/members' GET - devuelve TODOS los integrantes
'/members' POST - Crea UNO integrantes
'/members/<int:id_member>' GET - devuelve UNO integrante
'/members/<int:id_member>' PUT - modifica UNO integrante
'/members/<int:id_member>' DELETE - borra UNO integrante
"""


@app.route('/members', methods=['GET', 'POST'])
def handle_hello():
    response_body = {}
    # This is how you can use the Family datastructure by calling its methods
    if request.method == 'GET':
        members = jackson_family.get_all_members()
        response_body["hello"] = "world"
        response_body["family"] = members
        return response_body, 200
    if request.method == 'POST':
        data = request.json  # Recibo los datos del front (body)
        #  Ejecuto el método para agregar el member en la lista
        results = jackson_family.add_member(data)
        response_body['message'] = 'Miembro agregado'
        response_body['results'] = results
        return response_body, 200


@app.route('/members/<int:id>', methods=['GET', 'DELETE'])
def handle_member(id):
    if request.method == 'GET':
        results = jackson_family.get_member(id)
        if results == []:
            response_body = {'message': 'No encontrado'}
            return  response_body, 405
        response_body = {'member': results}
        return response_body, 200
    if request.method == 'DELETE':
        results = jackson_family.delete_member(id)
        response_body = {'message': 'Eliminado',
                         'results': results}
        return response_body, 200


# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)