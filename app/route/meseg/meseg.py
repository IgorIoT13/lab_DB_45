from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request

from app.domain.meseg import Meseg
from app.controller import meseg_controller

meseges = Blueprint("meseg", __name__, url_prefix="/api/v1/meseg")


@meseges.get('/')
def get_all_classes_lecturer():
    return make_response(jsonify(meseg_controller.get_all_relationship_data()), HTTPStatus.OK)


@meseges.post('/')
def create_meseg():
    context = request.get_json()
    meseg = Meseg.create_from_dto(context)
    meseg_controller.create(meseg)
    return make_response(jsonify(meseg.put_into_dto()), HTTPStatus.OK)


@meseges.put('/<int:meseg_id>')
def update_meseg(meseg_id):
    context = request.get_json()
    meseg = Meseg.create_from_dto(context)
    meseg_controller.update(meseg_id, meseg)
    return make_response(jsonify("meseg update"), HTTPStatus.OK)


@meseges.patch('/<int:meseg_id>')
def patch_meseg(meseg_id):
    context = request.get_json()
    meseg_controller.patch(meseg_id, context)
    return make_response(jsonify("meseg update"), HTTPStatus.OK)


@meseges.delete('/<int:meseg_id>')
def delete_meseg(meseg_id):
    meseg_controller.delete(meseg_id)
    return make_response(jsonify("Update meseg"), HTTPStatus.OK)