from app.dao import storismedia_dao
from app.services.general_service import GeneralService


class StorisMediaService(GeneralService):
    _dao = storismedia_dao