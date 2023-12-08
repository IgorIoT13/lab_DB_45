from app.dao.general_dao import GeneralDAO
from app.domain.autorisation import Autorisation


class AutorisationDAO(GeneralDAO):
    _domain_type = Autorisation
