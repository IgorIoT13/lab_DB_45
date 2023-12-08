from app.dao import images_dao
from app.services.general_service import GeneralService


class ImagesService(GeneralService):
    _dao = images_dao