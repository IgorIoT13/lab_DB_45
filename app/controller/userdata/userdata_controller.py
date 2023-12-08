from app.controller.general_controller import GeneralController
from app.services import userdata_service


class UserDataController(GeneralController):
    _service = userdata_service