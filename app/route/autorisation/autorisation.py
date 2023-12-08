from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request

from app.controller import autorisation_controller
from app.domain.autorisation import Autorisation

autorisations = Blueprint("autorisation", __name__, url_prefix="/api/v1/autorisation")


@autorisations.get('/')
def get_all_autorisation():
    return make_response(jsonify(autorisation_controller.find_all()), HTTPStatus.OK)


@autorisations.get('/<int:autorisation_id>')
def get_autorisation_by_id(autorisation_id):
    return make_response(jsonify(autorisation_controller.find_by_id(autorisation_id)), HTTPStatus.OK)


@autorisations.post('/')
def create_autorisation():
    context = request.get_json()
    autorisation = Autorisation.create_from_dto(context)
    autorisation_controller.create(autorisation)
    return make_response(jsonify(autorisation.put_into_dto()), HTTPStatus.OK)


@autorisations.put('/<int:autorisation_id>')
def update_autorisation(autorisation_id):
    context = request.get_json()
    autorisation = Autorisation.create_from_dto(context)
    autorisation_controller.update(autorisation_id, autorisation)
    return make_response(jsonify("Classe update"), HTTPStatus.OK)


@autorisations.patch('/<int:autorisation_id>')
def patch_autorisation(autorisation_id):
    context = request.get_json()
    autorisation_controller.patch(autorisation_id, context)
    return make_response(jsonify("Autorisation update"), HTTPStatus.OK)


@autorisations.delete('/<int:autorisation_id>')
def delete_autorisation(autorisation_id):
    autorisation_controller.delete(autorisation_id)
    return make_response(jsonify("Delete autorisation"), HTTPStatus.OK)


