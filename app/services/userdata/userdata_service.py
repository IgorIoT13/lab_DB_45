from app.dao import userdata_dao
from app.services.general_service import GeneralService


class UserDataService(GeneralService):
    _dao = userdata_dao