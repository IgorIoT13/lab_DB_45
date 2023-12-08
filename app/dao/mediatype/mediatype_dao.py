from app.dao.general_dao import GeneralDAO
from app.domain.mediatype import MediaType


class MediaTypeDAO(GeneralDAO):
    _domain_type = MediaType