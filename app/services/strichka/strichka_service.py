from app.dao import strichka_dao
from app.services.general_service import GeneralService


class StrichkaService(GeneralService):
    _dao = strichka_dao