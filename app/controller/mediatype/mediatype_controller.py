from app.controller.general_controller import GeneralController
from app.services import mediatype_service


class MediaTypeController(GeneralController):
    _service = mediatype_service