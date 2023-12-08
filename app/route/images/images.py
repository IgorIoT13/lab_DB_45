from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request

from app.domain.images import Images
from app.controller import images_controller

images = Blueprint("images", __name__, url_prefix="/api/v1/images")


@images.get('/')
def get_all_classes_lecturer():
    return make_response(jsonify(images_controller.get_all_relationship_data()), HTTPStatus.OK)


@images.post('/')
def create_image():
    context = request.get_json()
    image = Images.create_from_dto(context)
    images_controller.create(image)
    return make_response(jsonify(image.put_into_dto()), HTTPStatus.OK)


@images.put('/<int:image_id>')
def update_image(image_id):
    context = request.get_json()
    image = Images.create_from_dto(context)
    images_controller.update(image_id, image)
    return make_response(jsonify("image update"), HTTPStatus.OK)


@images.patch('/<int:image_id>')
def patch_image(image_id):
    context = request.get_json()
    images_controller.patch(image_id, context)
    return make_response(jsonify("image update"), HTTPStatus.OK)


@images.delete('/<int:image_id>')
def delete_image(image_id):
    images_controller.delete(image_id)
    return make_response(jsonify("Delete image"), HTTPStatus.OK)