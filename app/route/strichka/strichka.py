from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request

from app.domain.strichka import Strichka
from app.controller import strichka_controller

strickas = Blueprint("stricka", __name__, url_prefix="/api/v1/stricka")


@strickas.get('/')
def get_all_stricka():
    return make_response(jsonify(strichka_controller.get_all_relationship_data()), HTTPStatus.OK)


@strickas.post('/')
def create_stricka():
    context = request.get_json()
    stricka = Strichka.create_from_dto(context)
    strichka_controller.create(stricka)
    return make_response(jsonify(stricka.put_into_dto()), HTTPStatus.OK)


@strickas.put('/<int:stricka_id>')
def update_stricka(stricka_id):
    context = request.get_json()
    stricka = Strichka.create_from_dto(context)
    strichka_controller.update(stricka_id, stricka)
    return make_response(jsonify("stricka update"), HTTPStatus.OK)


@strickas.patch('/<int:stricka_id>')
def patch_stricka(stricka_id):
    context = request.get_json()
    strichka_controller.patch(stricka_id, context)
    return make_response(jsonify("stricka update"), HTTPStatus.OK)


@strickas.delete('/<int:stricka_id>')
def delete_stricka(stricka_id):
    strichka_controller.delete(stricka_id)
    return make_response(jsonify("Update stricka"), HTTPStatus.OK)