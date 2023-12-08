from app.controller.general_controller import GeneralController
from app.services import meseg_service


class MesegController(GeneralController):
    _service = meseg_service