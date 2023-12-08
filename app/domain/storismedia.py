from app import db


class StorisMedia(db.Model):
    IdMedia = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    Media = db.Column(db.BLOB, nullable=False)
    IdMediaType = db.Column(db.Integer, db.ForeignKey('MediaType.IdMediaType'), nullable=False)


    def put_into_dto(self):
        return {
            "IdMedia": self.IdMedia,
            "Media": self.Media,
            "IdMediaType": self.IdMediaType
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = StorisMedia(
            Media=dto_dict.get("Media"),
            IdMediaType=dto_dict.get("IdMediaType")
        )
        return obj
