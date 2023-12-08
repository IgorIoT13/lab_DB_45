from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request

from app.domain.mesegtype import MesegType
from app.controller import mesegtype_controller

meseg_types = Blueprint("mesegtype", __name__, url_prefix="/api/v1/mesegtype")


@meseg_types.get('/')
def get_all_meseg_type():
    return make_response(jsonify(mesegtype_controller.get_all_relationship_data()), HTTPStatus.OK)


@meseg_types.post('/')
def create_meseg_type():
    context = request.get_json()
    meseg_type = MesegType.create_from_dto(context)
    mesegtype_controller.create(meseg_type)
    return make_response(jsonify(meseg_type.put_into_dto()), HTTPStatus.OK)


@meseg_types.put('/<int:meseg_type_id>')
def update_meseg_type(meseg_type_id):
    context = request.get_json()
    meseg_type = MesegType.create_from_dto(context)
    mesegtype_controller.update(meseg_type_id, meseg_type)
    return make_response(jsonify("Classes lecturer update"), HTTPStatus.OK)


@meseg_types.patch('/<int:meseg_type_id>')
def patch_meseg_type(meseg_type_id):
    context = request.get_json()
    mesegtype_controller.patch(meseg_type_id, context)
    return make_response(jsonify("Classes lecture update"), HTTPStatus.OK)


@meseg_types.delete('/<int:meseg_type_id>')
def delete_meseg_type(meseg_type_id):
    mesegtype_controller.delete(meseg_type_id)
    return make_response(jsonify("Update classes lecturer"), HTTPStatus.OK)