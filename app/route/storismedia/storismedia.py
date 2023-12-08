from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request

from app.domain.storismedia import StorisMedia
from app.controller import storismedia_controller

storis_medias = Blueprint("storismedia", __name__, url_prefix="/api/v1/storismedia")


@storis_medias.get('/')
def get_all_storis_media():
    return make_response(jsonify(storismedia_controller.get_all_relationship_data()), HTTPStatus.OK)


@storis_medias.post('/')
def create_storis_media():
    context = request.get_json()
    storis_media = StorisMedia.create_from_dto(context)
    storismedia_controller.create(storis_media)
    return make_response(jsonify(storis_media.put_into_dto()), HTTPStatus.OK)


@storis_medias.put('/<int:storis_media_id>')
def update_storis_media(storis_media_id):
    context = request.get_json()
    storis_media = StorisMedia.create_from_dto(context)
    storismedia_controller.update(storis_media_id, storis_media)
    return make_response(jsonify("storis media update"), HTTPStatus.OK)


@storis_medias.patch('/<int:storis_media_id>')
def patch_storis_media(storis_media_id):
    context = request.get_json()
    storismedia_controller.patch(storis_media_id, context)
    return make_response(jsonify("storis media update"), HTTPStatus.OK)


@storis_medias.delete('/<int:storis_media_id>')
def delete_storis_media(storis_media_id):
    storismedia_controller.delete(storis_media_id)
    return make_response(jsonify("Update storis media"), HTTPStatus.OK)