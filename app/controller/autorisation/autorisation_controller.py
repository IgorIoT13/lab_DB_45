from app.controller.general_controller import GeneralController
from app.services import autorisation_service


class AutorisationController(GeneralController):
    _service = autorisation_service