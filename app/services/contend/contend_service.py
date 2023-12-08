from app.dao import contend_dao
from app.services.general_service import GeneralService


class ContendService(GeneralService):
    _dao = contend_dao
