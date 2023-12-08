from app.dao.general_dao import GeneralDAO
from app.domain.userins import UserIns


class UserInsDAO(GeneralDAO):
    _domain_type = UserIns