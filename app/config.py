import os

class BaseConfig:
  DEBUG = False
  TESTING = False
  SECRET_KEY = os.environ.get("SECRET_KEY")
  DATABASE_NAME = os.environ.get("DATABASE_NAME")
  DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
  DATABASE_USER = os.environ.get("DATABASE_USER")
  DATABASE_HOST = os.environ.get("DATABASE_HOST")
  DATABASE_PORT = os.environ.get("DATABASE_PORT")
  
class Development(BaseConfig):
  DEBUG = True

class Testing(BaseConfig):
  DEBUG = True
  TESTING = True
  DATABASE_NAME = "testdb"

class Production(BaseConfig):
  DEBUG = False

configuration = {
  "development":Development,
  "testing":Testing,
  "production":Production
  }
  