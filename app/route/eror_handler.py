from http import HTTPStatus
from flask import Blueprint, Response, make_response


err_handler_bp = Blueprint('errors', __name__)


@err_handler_bp.app_errorhandler(HTTPStatus.NOT_FOUND)
def handler_404(error):
    return make_response("Object not fount", HTTPStatus.NOT_FOUND)


@err_handler_bp.app_errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
def handle_422(error):
    return make_response("Input data is wrong or not full", HTTPStatus.UNPROCESSABLE_ENTITY)


@err_handler_bp.app_errorhandler(HTTPStatus.CONFLICT)
def handle_409(error):
    return make_response("Such object is already exists in DB", HTTPStatus.CONFLICT)