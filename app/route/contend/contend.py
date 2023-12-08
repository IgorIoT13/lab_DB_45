from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request

from app.domain.contend import Contend
from app.controller import contend_controller

contends = Blueprint("contend", __name__, url_prefix="/api/v1/contend")


@contends.get('/')
def get_all_contend():
    return make_response(jsonify(contend_controller.find_all()), HTTPStatus.OK)


@contends.post('/')
def create_contend():
    context = request.get_json()
    contend = Contend.create_from_dto(context)
    contend_controller.create(contend)
    return make_response(jsonify(contend.put_into_dto()), HTTPStatus.OK)


@contends.put('/<int:contend_id>')
def update_contend(contend_id):
    context = request.get_json()
    contend = Contend.create_from_dto(context)
    contend_controller.update(contend_id, contend)
    return make_response(jsonify("contend update"), HTTPStatus.OK)


@contends.patch('/<int:contend_id>')
def patch_classes_lecturer(contend_id):
    context = request.get_json()
    contend_controller.patch(contend_id, context)
    return make_response(jsonify("contend update"), HTTPStatus.OK)


@contends.delete('/<int:contend_id>')
def delete_classes_lecturer(contend_id):
    contend_controller.delete(contend_id)
    return make_response(jsonify("Update contend"), HTTPStatus.OK)