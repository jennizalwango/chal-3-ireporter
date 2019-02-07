import datetime
from app import DatabaseConnection

cursor = DatabaseConnection.cursor()

class Incident:
  cursor.execute('''CREATE TABLE IF NOT EXISTS incident
                (incident_id SERIAL PRIMARY KEY,
                incident_type VARCHAR(50) NOT NULL,
                title VARCHAR(50) NOT NULL,
                created_by INTEGER NOT NULL,
                location VARCHAR(50) NOT NULL,
                status  VARCHAR(50) DEFAULT 'draft',
                comment VARCHAR(50),
                created_on TIMESTAMP DEFAULT Now(),
                FOREIGN KEY (created_by)
                  REFERENCES users (user_id)
                  ON UPDATE CASCADE ON DELETE CASCADE);
                ''')

  def __init__(self, **kwargs):
    self.incident_type = kwargs["incident_type"]
    self.title = kwargs["title"]
    self.created_by = kwargs["created_by"]
    self.location = kwargs["location"]
    self.status = kwargs["status"]
    self.comment = kwargs["comment"]


  #  save is the same as create incident in the database
  def save(self):
    cursor = DatabaseConnection.cursor()

    query = """
            INSERT INTO incident(incident_type, title, created_by, location, status, comment)
            VALUES('{}','{}', '{}', '{}', '{}', '{}')""".format(self.incident_type, self.title, self.created_by, self.location, self.status, self.comment)
    cursor.execute(query)
    DatabaseConnection.commit()

  @staticmethod
  def check_created_incident(created_by):
    cursor = DatabaseConnection.cursor()
    #this query returns the most recent id in the table and it requires the table name and the column name want to use
    query = """SELECT currval(pg_get_serial_sequence('{}', '{}'))""".format("incident", "incident_id")
    cursor.execute(query)
    Incidents = cursor.fetchone()
    #return the id which is in position zero of list incident
    return Incidents[0]

  @staticmethod
  def get_an_incident(incident_id):
    cursor = DatabaseConnection.cursor()
    query = "SELECT row_to_json(incident) FROM incident WHERE incident_id = '{}';".format(incident_id)
    cursor.execute(query)
    incidents = cursor.fetchone()
    return incidents

  @staticmethod
  def get_all_incident():
    DatabaseConnection.cursor()
    query = "SELECT row_to_json(incident) FROM incident"
    cursor.execute(query)
    all_incidents = cursor.fetchall()
    return all_incidents

  @staticmethod
  def update_location(incident_id, location):
    DatabaseConnection.cursor()
    query = "UPDATE incident SET location = '{}' WHERE incident_id = '{}';".format(location, incident_id)
    cursor.execute(query)
   
  @staticmethod
  def update_comment(incident_id, comment):
    DatabaseConnection.cursor()
    query = "UPDATE incident SET location = '{}' WHERE incident_id = '{}';".format(comment, incident_id)
    cursor.execute(query)

  @staticmethod
  def update_the_status(incident_id, status):
    DatabaseConnection.cursor()
    query = "UPDATE incident SET status = '{}' WHERE incident_id = '{}';".format(status, incident_id)
    cursor.execute(query)


  