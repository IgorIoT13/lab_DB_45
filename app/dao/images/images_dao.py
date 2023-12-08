from app.dao.general_dao import GeneralDAO
from app.domain.images import Images


class ImagesDAO(GeneralDAO):
    _domain_type = Images