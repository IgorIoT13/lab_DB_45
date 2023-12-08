from app.dao.general_dao import GeneralDAO
from app.domain.userdata import UserData


class UserDataDAO(GeneralDAO):
    _domain_type = UserData