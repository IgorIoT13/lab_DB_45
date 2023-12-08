from app.controller.general_controller import GeneralController
from app.services import contend_service


class ContendController(GeneralController):
    _service = contend_service