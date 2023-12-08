from app.dao.general_dao import GeneralDAO
from app.domain.storismedia import StorisMedia


class StorisMediaDAO(GeneralDAO):
    _domain_type = StorisMedia