from app.controller.general_controller import GeneralController
from app.services import images_service


class ImagesController(GeneralController):
    _service = images_service