from app.dao.general_dao import GeneralDAO
from app.domain.mesegtype import MesegType


class MesegTypeDAO(GeneralDAO):
    _domain_type = MesegType