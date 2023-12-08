from app.controller.general_controller import GeneralController
from app.services import reaction_service


class ReactionController(GeneralController):
    _service = reaction_service