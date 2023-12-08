from app import db


class Contend(db.Model):
    IdMedia = db.Column(db.Integer, db.ForeignKey('StorisMedia.IdMedia'), nullable=False, primary_key=True)
    Date = db.Column(db.Date)
    Name = db.Column(db.String, nullable=True)

    def put_into_dto(self):
        return {
            "IdMedia": self.IdMedia,
            "Date": self.Date,
            "Name": self.Name
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Contend(
            IdMedia=dto_dict.get("IdMedia"),
            Date=dto_dict.get("Date"),
            Name=dto_dict.get("Name")
        )
        return obj