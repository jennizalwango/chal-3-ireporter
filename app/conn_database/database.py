import os
import psycopg2
from app import app
from app import config

class DatabaseConnection:
  def __init__(self):
    try:
        self.connection = psycopg2.connect(
          database = config.DATABASE_NAME, 
          password = config.DATABASE_PASSWORD, 
          user = config.DATABASE_USER, 
          host = config.DATABASE_HOST, 
          port = config.DATABASE_PORT
          )
        self.connection.autocommit = True
        self.dict_cursor = self.connection.cursor()
        self.create_tables()
    except Exception as ex:
      print("Database connection error: {}".format(str(ex)))
            

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
