import os
import psycopg2
from app import app
from app.config import configuration

config = configuration.get(os.environ.get("APP_ENV", "development"))
config1 = configuration.get(os.environ.get("TEST_ENV", "testing"))
app.config.from_object(config)

class DatabaseConnection:
  def __init__(self):
    try:
      if os.environ.get("APP_ENV") == "development":
        self.connection = psycopg2.connect(
          database = config.DATABASE_NAME, 
          password = config.DATABASE_PASSWORD, 
          user = config.DATABASE_USER, 
          host = config.DATABASE_HOST, 
          port = 5432)
        self.connection.autocommit = True
        self.dict_cursor = self.connection.cursor()
        self.create_tables()
      if os.environ.get("APP_ENV1") == "testing":
        self.connection = psycopg2.connect(
          database = config.DATABASE_NAME,
          password = config.DATABASE_PASSWORD,
          user = config.DATABASE_USER,
          host = config.DATABASE_HOST, 
          port = 5432)

      if os.environ.get("APP_ENV2") == "production":
        if os.environ.get("database") == 'heroku':
         self.connection = psycopg2.connect(
           database = "d7lrmgbjs3a0im",
           user="qzgoznoygmxmvo", password="da463569b47a5c48c1c7e0b19bf91e3535c4e3ace4bba892260bf9850c9f6e88",host="ec2-23-21-165-188.compute-1.amazonaws.com",
           port=5432
         )
        else: 
          self.connection = psycopg2.connect(database ="testdb")
    except Exception as ex:
      print("Database connection error: "+str(ex))

            
  def create_tables(self):
    create_all_tables = (
          """CREATE TABLE IF NOT EXISTS users
                (user_id SERIAL PRIMARY KEY   NOT NULL,
                username VARCHAR(225) NOT NULL,
                password VARCHAR(225) NOT NULL,
                email VARCHAR(225) NOT NULL ,
                phone_number VARCHAR(225) NOT NULL ,
                is_admin VARCHAR(225) NOT NULL);
                """,

          """CREATE TABLE IF NOT EXISTS incident
                (incident_id SERIAL PRIMARY KEY ,
                incident_type VARCHAR(225) NOT NULL ,
                title VARCHAR(225) NOT NULL ,
                created_by INTEGER NOT NULL ,
                location VARCHAR(225) NOT NULL ,
                status  VARCHAR(225) DEFAULT 'draft',
                comment VARCHAR(225),
                created_on TIMESTAMP DEFAULT Now(),
                FOREIGN KEY (created_by)
                  REFERENCES users (user_id)
                  ON UPDATE CASCADE ON DELETE CASCADE);
                  """,
          """CREATE TABLE IF NOT EXISTS blacklist_token
                  (id SERIAL PRIMARY KEY NOT NULL,
                  token VARCHAR(50) NOT NULL,
                  Blacklisted_on TIMESTAMP NOT NULL);
                  """
                )
    for table in create_all_tables:
      self.dict_cursor.execute(table)

  def drop_tables(self):
    drop_queries = (
      """DROP TABLE IF EXISTS users CASCADE
      """,
      """DROP TABLE IF EXISTS incident CASCADE
      """,
      """DROP TABLE IF EXISTS blacklist_token CASCADE
      """
      )
    for query in drop_queries:
        self.dict_cursor.execute(query)
