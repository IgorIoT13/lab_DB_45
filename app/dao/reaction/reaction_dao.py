from app.dao.general_dao import GeneralDAO
from app.domain.reaction import Reaction


class ReactionDAO(GeneralDAO):
    _domain_type = Reaction