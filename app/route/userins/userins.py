from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request

from app.domain.userins import UserIns
from app.controller import userins_controller

users_ins = Blueprint("userins", __name__, url_prefix="/api/v1/userins")


@users_ins.get('/')
def get_all_user_ins():
    return make_response(jsonify(userins_controller.get_all_relationship_data()), HTTPStatus.OK)


@users_ins.post('/')
def create_user_ins():
    context = request.get_json()
    user_ins = UserIns.create_from_dto(context)
    userins_controller.create(user_ins)
    return make_response(jsonify(user_ins.put_into_dto()), HTTPStatus.OK)


@users_ins.put('/<int:user_ins_id>')
def update_user_ins(user_ins_id):
    context = request.get_json()
    user_ins = UserIns.create_from_dto(context)
    userins_controller.update(user_ins_id, user_ins)
    return make_response(jsonify("user ins update"), HTTPStatus.OK)


@users_ins.patch('/<int:user_ins_id>')
def patch_user_ins(user_ins_id):
    context = request.get_json()
    userins_controller.patch(user_ins_id, context)
    return make_response(jsonify("user ins update"), HTTPStatus.OK)


@users_ins.delete('/<int:user_ins_id>')
def delete_user_ins(user_ins_id):
    userins_controller.delete(user_ins_id)
    return make_response(jsonify("Update user ins"), HTTPStatus.OK)