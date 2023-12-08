from app import db


class MediaType(db.Model):
    IdMediaType = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    MediaType = db.Column(db.String(45), nullable=False)

    def put_into_dto(self):
        return {
            "IdMediaType": self.IdMediaType,
            "MediaType": self.MediaType
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = MediaType(
            MediaType=dto_dict.get("MediaType")
        )
        return obj