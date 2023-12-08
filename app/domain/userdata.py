from app import db


class UserData(db.Model):
    IdUser = db.Column(db.Integer, db.ForeignKey('UserIns.IdUser'), nullable=False, primary_key=True)
    Nomer = db.Column(db.String(45), nullable=False)
    MainImgId = db.Column(db.Integer,db.ForeignKey('images.IdImg'), nullable=False, primary_key=True)
    DataCreate = db.Column(db.Date, nullable=False)

    def put_into_dto(self):
        return {
            "IdUser": self.IdUser,
            "Nomer": self.Nomer,
            "MainImgId": self.MainImgId,
            "DataCreate": self.DataCreate
        }

    @staticmethod
    def create_from_dto(dto_dict):
        obj = UserData(
            IdUser=dto_dict.get("IdUser"),
            Nomer=dto_dict.get("Nomer"),
            MainImgId=dto_dict.get("MainImgId"),
            DataCreate=dto_dict.get("DataCreate")
        )
        return obj