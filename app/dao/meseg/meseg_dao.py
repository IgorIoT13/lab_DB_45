from app.dao.general_dao import GeneralDAO
from app.domain.meseg import Meseg


class MesegDAO(GeneralDAO):
    _domain_type = Meseg