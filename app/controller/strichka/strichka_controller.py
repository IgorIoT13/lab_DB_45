from app.controller.general_controller import GeneralController
from app.services import strichka_service


class StrichkaController(GeneralController):
    _service = strichka_service