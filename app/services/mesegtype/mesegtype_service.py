from app.dao import mesegtype_dao
from app.services.general_service import GeneralService


class MesegTypeService(GeneralService):
    _dao = mesegtype_dao