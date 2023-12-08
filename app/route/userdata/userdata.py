from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request

from app.domain.userdata import UserData
from app.controller import userdata_controller

users_data = Blueprint("userdata", __name__, url_prefix="/api/v1/userdata")


@users_data.get('/')
def get_all_classes_lecturer():
    return make_response(jsonify(userdata_controller.get_all_relationship_data()), HTTPStatus.OK)


@users_data.post('/')
def create_user_data():
    context = request.get_json()
    user_data = UserData.create_from_dto(context)
    userdata_controller.create(user_data)
    return make_response(jsonify(user_data.put_into_dto()), HTTPStatus.OK)


@users_data.put('/<int:user_data_id>')
def update_user_data(user_data_id):
    context = request.get_json()
    user_data = UserData.create_from_dto(context)
    userdata_controller.update(user_data_id, user_data)
    return make_response(jsonify("user data update"), HTTPStatus.OK)


@users_data.patch('/<int:user_data_id>')
def patch_user_data(user_data_id):
    context = request.get_json()
    userdata_controller.patch(user_data_id, context)
    return make_response(jsonify("user data update"), HTTPStatus.OK)


@users_data.delete('/<int:user_data_id>')
def delete_user_data(user_data_id):
    userdata_controller.delete(user_data_id)
    return make_response(jsonify("Update user data"), HTTPStatus.OK)