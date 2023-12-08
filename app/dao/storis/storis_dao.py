from app.dao.general_dao import GeneralDAO
from app.domain.storis import Storis


class StorisDAO(GeneralDAO):
    _domain_type = Storis