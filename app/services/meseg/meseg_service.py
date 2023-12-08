from app.dao import meseg_dao
from app.services.general_service import GeneralService


class MesegService(GeneralService):
    _dao = meseg_dao