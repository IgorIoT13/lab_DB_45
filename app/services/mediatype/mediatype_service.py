from app.dao import mediatype_dao
from app.services.general_service import GeneralService


class MediaTypeService(GeneralService):
    _dao = mediatype_dao