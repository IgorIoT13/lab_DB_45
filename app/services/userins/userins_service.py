from app.dao import userins_dao
from app.services.general_service import GeneralService


class UserInsService(GeneralService):
    _dao = userins_dao