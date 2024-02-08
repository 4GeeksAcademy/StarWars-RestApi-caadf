from flask import Blueprint, request, jsonify
api = Blueprint('api', __name__)


""" Usar rutas (GET; POST; PUT; DELETE) """

@api.route('/test')
def test():
    return jsonify({"msg": "Testing API Routes"}), 200
