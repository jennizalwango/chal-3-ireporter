import datetime
from app.conn_database.database import DatabaseConnection

db = DatabaseConnection()
cursor = db.dict_cursor

class Incident:
  def __init__(self, **kwargs):
    self.incident_type = kwargs["incident_type"]
    self.title = kwargs["title"]
    self.created_by = kwargs["created_by"]
    self.location = kwargs["location"]
    self.status = kwargs["status"]
    self.comment = kwargs["comment"] 
          

  #  save is the same as create incident in the database
  def save(self):
    query = """
            INSERT INTO incident(incident_type, title, created_by, location, status, comment)
            VALUES('{}','{}', '{}', '{}', '{}', '{}')""".format(self.incident_type, self.title, self.created_by, self.location, self.status, self.comment)
    cursor.execute(query)
   

  @staticmethod
  def check_created_incident(created_by):
    #this query returns the most recent id in the table and it requires the table name and the column name want to use
    query = """SELECT currval(pg_get_serial_sequence('{}', '{}'))""".format("incident", "incident_id")
    cursor.execute(query)
    Incidents = cursor.fetchone()
    #return the id which is in position zero of list incident
    return Incidents[0]

  @staticmethod
  def get_an_incident(incident_id):
    query = "SELECT row_to_json(incident) FROM incident WHERE incident_id = '{}';".format(incident_id)
    cursor.execute(query)
    incidents = cursor.fetchone()
    return incidents

  @staticmethod
  def get_all_incident():
    query = "SELECT row_to_json(incident) FROM incident"
    cursor.execute(query)
    all_incidents = cursor.fetchall()
    return all_incidents

  @staticmethod
  def check_incident_id(incident_id):
    query = "SELECT row_to_json(incident_id) FROM incident WHERE incident_id = '{}';".format(incident_id)
    cursor.execute(query)
    checking_incident_id = cursor.fetchone()
    return checking_incident_id

  @staticmethod
  def update_location(user_id, incident_id, location):
    query = "UPDATE incident SET location = '{}' WHERE incident_id = '{}';".format(location, incident_id)
    cursor.execute(query)
   
  @staticmethod
  def update_comment(user_id, incident_id, comment):
    query = "UPDATE incident SET comment = '{}' WHERE incident_id = '{}';".format(comment, incident_id)
    cursor.execute(query)

  @staticmethod
  def update_the_status(user_id, incident_id, status):
    query = "UPDATE incident SET status = '{}' WHERE incident_id = '{}';".format(status, incident_id)
    cursor.execute(query)
  
  @staticmethod
  def get_user_type(user_id):
    query = "SELECT is_admin FROM users WHERE user_id = '{}'".format(user_id)
    cursor.execute(query)
    get_the_user = cursor.fetchone()
    return get_the_user[0]

  @staticmethod
  def delete_incident(user_id, incident_id):
    query = "DELETE FROM incident WHERE incident_id = '{}'".format(incident_id)
    cursor.execute(query)

#check for the record matching the user's id and incident id
  @staticmethod
  def  check_if_user_id_matches_the_incident_id(created_by, incident_id):
    query = "SELECT status FROM incident WHERE created_by = '{}' AND \
      incident_id = '{}'".format(created_by, incident_id)
    cursor.execute(query)
    incident_matching = cursor.fetchone()
    return incident_matching
    