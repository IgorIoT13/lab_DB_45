from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
  pass


app = Flask(__name__)

db = SQLAlchemy(model_class=Base)
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ihor14102005@localhost:3306/lab_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from app.domain.autorisation import Autorisation
from app.domain.contend import Contend
from app.domain.images import Images
from app.domain.mediatype import MediaType
from app.domain.meseg import Meseg
from app.domain.mesegtype import MesegType
from app.domain.reaction import Reaction
from app.domain.storis import Storis
from app.domain.storismedia import StorisMedia
from app.domain.strichka import Strichka
from app.domain.userdata import UserData
from app.domain.userins import UserIns




with app.app_context():
    db.create_all()



from app.route.autorisation.autorisation import autorisations
from app.route.contend.contend import contends
from app.route.eror_handler import err_handler_bp
from app.route.images.images import images
from app.route.mediatype.mediatype import media_types
from app.route.meseg.meseg import meseges
from app.route.mesegtype.mesegtype import meseg_types
from app.route.reaction.reaction import reactions
from app.route.storis.storis import storises
from app.route.storismedia.storismedia import storis_medias
from app.route.strichka.strichka import strickas
from app.route.userdata.userdata import users_data
from app.route.userins.userins import users_ins


app.register_blueprint(autorisations)
app.register_blueprint(contends)
app.register_blueprint(images)
app.register_blueprint(media_types)
app.register_blueprint(meseges)
app.register_blueprint(meseg_types)
app.register_blueprint(reactions)
app.register_blueprint(storises)
app.register_blueprint(storis_medias)
app.register_blueprint(strickas)
app.register_blueprint(users_data)
app.register_blueprint(users_ins)
app.register_blueprint(err_handler_bp)

