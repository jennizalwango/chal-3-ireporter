import os
import psycopg2
from flask import Flask
from passlib.hash import sha256_crypt
from app.config import configuration

config = configuration.get(os.environ.get("APP_ENV", "development"))
app = Flask(__name__)
app.config.from_object(config)


from app.routes.user_routes import UserUrl
UserUrl.get_user_routes(app)

from app.routes.incident_routes import IncidentUrl
IncidentUrl.get_incident_routes(app)

from app.routes.incident_routes import UpdateUrl
UpdateUrl.update_the_comment_routes(app)

from app.routes.incident_routes import UpdateStatus
UpdateStatus.update_status(app)
