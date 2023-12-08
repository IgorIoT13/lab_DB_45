from app.dao import autorisation_dao
from app.services.general_service import GeneralService


class AutorisationService(GeneralService):
    _dao = autorisation_dao
