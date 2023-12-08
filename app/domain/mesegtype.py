from app import db


class MesegType(db.Model):
    IdMesegType = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    MesegType = db.Column(db.String(45), nullable=False)

    def put_into_dto(self):
        return {
            "IdMesegType": self.IdMesegType,
            "MesegType": self.MesegType
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = MesegType(
            MesegType=dto_dict.get("MesegType")
        )
        return obj
