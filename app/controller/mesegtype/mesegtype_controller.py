from app.controller.general_controller import GeneralController
from app.services import mesegtype_service


class MesegTypeController(GeneralController):
    _service = mesegtype_service