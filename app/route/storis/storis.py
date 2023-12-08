from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request

from app.domain.storis import Storis
from app.controller import storis_controller

storises = Blueprint("storis", __name__, url_prefix="/api/v1/storis")


@storises.get('/')
def get_all_storis():
    return make_response(jsonify(storis_controller.get_all_relationship_data()), HTTPStatus.OK)


@storises.post('/')
def create_storis():
    context = request.get_json()
    storis = Storis.create_from_dto(context)
    storis_controller.create(storis)
    return make_response(jsonify(storis.put_into_dto()), HTTPStatus.OK)


@storises.put('/<int:storis_id>')
def update_storis(storis_id):
    context = request.get_json()
    storis = Storis.create_from_dto(context)
    storis_controller.update(storis_id, storis)
    return make_response(jsonify("storis update"), HTTPStatus.OK)


@storises.patch('/<int:storis_id>')
def patch_storis(storis_id):
    context = request.get_json()
    storis_controller.patch(storis_id, context)
    return make_response(jsonify("storis update"), HTTPStatus.OK)


@storises.delete('/<int:storis_id>')
def delete_storis(storis_id):
    storis_controller.delete(storis_id)
    return make_response(jsonify("Update storis"), HTTPStatus.OK)