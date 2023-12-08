from app import db


class UserIns(db.Model):
    __tablename__ = 'UserIns'
    IdUser = db.Column(db.Integer, db.ForeignKey('Autorisation.IdUser'), nullable=False, index=True, primary_key=True)
    UserName = db.Column(db.String(45), nullable=False)

    user_data = db.relationship('UserData', backref='userins', uselist=False, lazy=True)
    strichka = db.relationship('Strichka', backref='userins', lazy=True)

    storis = db.relationship('Storis', backref='userins', lazy=True)
    images = db.relationship('Images', backref='userins', lazy=True)

    def put_into_dto(self):
        return {
            "IdUser": self.IdUser,
            "UserName": self.UserName
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = UserIns(
            IdUser=dto_dict.get("IdUser"),
            UserName=dto_dict.get("UserName")
        )
        return obj
