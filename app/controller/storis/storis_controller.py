from app.controller.general_controller import GeneralController
from app.services import storis_service


class StorisController(GeneralController):
    _service = storis_service