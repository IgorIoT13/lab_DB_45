from app.dao import reaction_dao
from app.services.general_service import GeneralService


class ReactionService(GeneralService):
    _dao = reaction_dao