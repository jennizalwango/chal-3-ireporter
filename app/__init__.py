import os
import psycopg2
from flask import Flask
from passlib.hash import sha256_crypt
from app.config import configuration

app = Flask(__name__)
config = configuration.get(os.environ.get("APP_ENV", "development"))
app.config.from_object(config)

# DatabaseConnection = psycopg2.connect(
#   database = config.DATABASE_NAME, 
#   password = config.DATABASE_PASSWORD, 
#   user = config.DATABASE_USER, 
#   host = config.DATABASE_HOST, 
#   port = 5432
#   )
if os.getenv('db') == 'heroku':
    conn = psycopg2.connect(database = "d7lrmgbjs3a0im",user="qzgoznoygmxmvo", password="da463569b47a5c48c1c7e0b19bf91e3535c4e3ace4bba892260bf9850c9f6e88",host="ec2-23-21-165-188.compute-1.amazonaws.com",port=5432)
else: 
  DatabaseConnection = psycopg2.connect(database ="testdb")
    



from app.routes.user_routes import UserUrl
UserUrl.get_user_routes(app)

from app.routes.incident_routes import IncidentUrl
IncidentUrl.get_incident_routes(app)

from app.routes.incident_routes import UpdateUrl
UpdateUrl.update_the_comment_routes(app)

from app.routes.incident_routes import UpdateStatus
UpdateStatus.update_status(app)
