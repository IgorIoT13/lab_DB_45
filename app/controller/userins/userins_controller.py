from app.controller.general_controller import GeneralController
from app.services import userins_service


class UserInsController(GeneralController):
    _service = userins_service