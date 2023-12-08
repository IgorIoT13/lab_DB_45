from app import db


class Images(db.Model):
    IdImg = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    IdUser = db.Column(db.Integer, db.ForeignKey('UserIns.IdUser'), nullable=False)
    Img = db.Column(db.BLOB)

    def put_into_dto(self):
        return {
            "IdImg": self.IdImg,
            "IdUser": self.IdUser,
            "Img": self.Img
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Images(
            IdUser=dto_dict.get("IdUser"),
            Img=dto_dict.get("Img")
        )
        return obj