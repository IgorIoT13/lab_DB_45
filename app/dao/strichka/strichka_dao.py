from app.dao.general_dao import GeneralDAO
from app.domain.strichka import Strichka


class StrichkaDAO(GeneralDAO):
    _domain_type = Strichka