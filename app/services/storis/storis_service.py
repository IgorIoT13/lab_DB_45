from app.dao import storis_dao
from app.services.general_service import GeneralService


class StorisService(GeneralService):
    _dao = storis_dao