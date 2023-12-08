from app import db


class Reaction(db.Model):
    IdReaction = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    Reaction = db.Column(db.String(45), nullable=False)

    def put_into_dto(self):
        return {
            "IdReaction": self.IdReaction,
            "Reaction": self.Reaction
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Reaction(
            Reaction=dto_dict.get("Reaction")
        )
        return obj