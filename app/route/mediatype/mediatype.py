from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request

from app.domain.mediatype import MediaType
from app.controller import mediatype_controller

media_types = Blueprint("mediatype", __name__, url_prefix="/api/v1/mediatype")


@media_types.get('/')
def get_all_classes_lecturer():
    return make_response(jsonify(mediatype_controller.get_all_relationship_data()), HTTPStatus.OK)


@media_types.post('/')
def create_media_type():
    context = request.get_json()
    mediatype = MediaType.create_from_dto(context)
    mediatype_controller.create(mediatype)
    return make_response(jsonify(mediatype.put_into_dto()), HTTPStatus.OK)


@media_types.put('/<int:media_type_id>')
def update_media_type(media_type_id):
    context = request.get_json()
    mediatype = MediaType.create_from_dto(context)
    mediatype_controller.update(media_type_id, mediatype)
    return make_response(jsonify("media type update"), HTTPStatus.OK)


@media_types.patch('/<int:media_type_id>')
def patch_media_type(media_type_id):
    context = request.get_json()
    mediatype_controller.patch(media_type_id, context)
    return make_response(jsonify("media type update"), HTTPStatus.OK)


@media_types.delete('/<int:media_type_id>')
def delete_media_type(media_type_id):
    mediatype_controller.delete(media_type_id)
    return make_response(jsonify("Update media type"), HTTPStatus.OK)