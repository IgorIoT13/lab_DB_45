from app.services.autorisation.autorisation_service import AutorisationService
from app.services.contend.contend_service import ContendService
from app.services.images.images_service import ImagesService
from app.services.mediatype.mediatype_service import MediaTypeService
from app.services.meseg.meseg_service import MesegService
from app.services.mesegtype.mesegtype_service import MesegTypeService
from app.services.reaction.reaction_service import ReactionService
from app.services.storis.storis_service import StorisService
from app.services.storismedia.storismedia_service import StorisMediaService
from app.services.strichka.strichka_service import StrichkaService
from app.services.userdata.userdata_service import UserDataService
from app.services.userins.userins_service import UserInsService

autorisation_service = AutorisationService()
contend_service = ContendService()
images_service = ImagesService()
mediatype_service = MediaTypeService()
meseg_service = MesegService()
mesegtype_service = MesegTypeService()
reaction_service = ReactionService()
storis_service = StorisService()
storismedia_service = StorisMediaService()
strichka_service = StrichkaService()
userdata_service = UserDataService()
userins_service = UserInsService()