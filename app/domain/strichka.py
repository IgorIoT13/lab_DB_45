from app import db


class Strichka(db.Model):
    IdStoris = db.Column(db.Integer, db.ForeignKey('Storis.IdStoris'), nullable=False, primary_key=True)
    IdUser = db.Column(db.Integer, db.ForeignKey('UserIns.IdUser'), nullable=False)

    def put_into_dto(self):
        return {
            "IdStoris": self.IdStoris,
            "IdUser": self.IdUser
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Strichka(
            IdStoris=dto_dict.get("IdStoris"),
            IdUser=dto_dict.get("IdUser")
        )
        return obj