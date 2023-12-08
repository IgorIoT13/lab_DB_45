from app import db


class Storis(db.Model):
    IdStoris = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    IdMedia = db.Column(db.Integer, db.ForeignKey('StorisMedia.IdMedia'),nullable=False, primary_key=True)
    IdUser = db.Column(db.Integer, db.ForeignKey('UserIns.IdUser'), nullable=False)
    LikeS = db.Column(db.Integer, nullable=False)

    def put_into_dto(self):
        return {
            "IdStoris": self.IdStoris,
            "IdMedia": self.IdMedia,
            "IdUser": self.IdUser,
            "LikeS": self.LikeS
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Storis(
            IdMedia=dto_dict.get("IdMedia"),
            IdUser=dto_dict.get("IdUser"),
            LikeS=dto_dict.get("LikeS")
        )
        return obj
