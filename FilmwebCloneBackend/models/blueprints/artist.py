from .. import db
from enums import UserGender
from ..utils.utc_now import utcnow

class Artist():
  first_name = db.Column(db.String(20), nullable = False)
  last_name = db.Column(db.String(40), nullable = False)
  nationality = db.Column(db.String(70), nullable = True)
  description = db.Column(db.String(1000), nullable = True)
  gender = db.Column(db.Enum(UserGender), nullable = True)
  height = db.Column(db.Integer, nullable = True)
  birth_date = db.Column(db.DateTime, nullable = False, server_default = utcnow())
  file_path = db.Column(db.String(500), nullable = True)