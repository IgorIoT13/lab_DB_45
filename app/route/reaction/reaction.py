from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, request

from app.domain.reaction import Reaction
from app.controller import reaction_controller

reactions = Blueprint("reactions", __name__, url_prefix="/api/v1/reactions")


@reactions.get('/')
def get_all_reactions():
    return make_response(jsonify(reaction_controller.get_all_relationship_data()), HTTPStatus.OK)


@reactions.post('/')
def create_reactions():
    context = request.get_json()
    classes_lecturer = Reaction.create_from_dto(context)
    reaction_controller.create(classes_lecturer)
    return make_response(jsonify(classes_lecturer.put_into_dto()), HTTPStatus.OK)


@reactions.put('/<int:reactions_id>')
def update_reactions(reactions_id):
    context = request.get_json()
    classes_lecturer = Reaction.create_from_dto(context)
    reaction_controller.update(reactions_id, classes_lecturer)
    return make_response(jsonify("reactions update"), HTTPStatus.OK)


@reactions.patch('/<int:reactions_id>')
def patch_reactions(reactions_id):
    context = request.get_json()
    reaction_controller.patch(reactions_id, context)
    return make_response(jsonify("reactions update"), HTTPStatus.OK)


@reactions.delete('/<int:reactions_id>')
def delete_reactions(reactions_id):
    reaction_controller.delete(reactions_id)
    return make_response(jsonify("Update reactions"), HTTPStatus.OK)