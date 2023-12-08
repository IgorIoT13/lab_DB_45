from app.controller.general_controller import GeneralController
from app.services import storismedia_service


class StorisMediaController(GeneralController):
    _service = storismedia_service