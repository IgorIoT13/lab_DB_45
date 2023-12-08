from app import db


class Autorisation (db.Model):
    __tablename__ = 'Autorisation'
    IdUser = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    Login = db.Column(db.String(45), nullable=False, index=True)
    Pasword = db.Column(db.String(45), nullable=False, index=True)

    user_ins = db.relationship('UserIns', backref='autorisation', uselist=False, lazy=True)

    def put_into_dto(self):
        return {
            "IdUser": self.IdUser,
            "Login": self.Login,
            "Pasword": self.Pasword
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = Autorisation(
            Login=dto_dict.get("Login"),
            Pasword=dto_dict.get("Pasword")
        )
        return obj