from app import db


class Meseg(db.Model):
    IdMeseg = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    IdUser = db.Column(db.Integer, db.ForeignKey('UserIns.IdUser'), nullable=False)
    Meseg = db.Column(db.String)
    IdMedia = db.Column(db.Integer, db.ForeignKey('StorisMedia.IdMedia'))
    IdMesegType = db.Column(db.Integer, db.ForeignKey('MesegType.IdMesegType'), nullable=False)
    IdReaction = db.Column(db.Integer, db.ForeignKey('Reaction.IdReaction'), nullable=False)

    def put_into_dto(self):
        return {
            "IdMeseg": self.IdMeseg,
            "IdUser": self.IdUser,
            "Meseg": self.Meseg,
            "IdMedia": self.IdMedia,
            "IdMesegType": self.IdMesegType,
            "IdReaction": self.IdReaction
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Meseg(
            IdUser=dto_dict.get("IdUser"),
            Meseg=dto_dict.get("Meseg"),
            IdMedia=dto_dict.get("IdMedia"),
            IdMesegType=dto_dict.get("IdMesegType"),
            IdReaction=dto_dict.get("IdReaction")
        )
        return obj