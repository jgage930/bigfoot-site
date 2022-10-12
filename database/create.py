### Methods for creating database models
from database.models import Sighting
from database.setup import create_connection
import sqlite3

DATABASE = r'/home/jgage/Documents/Projects/bigfoot-site/database.db'

def insert_sighting(sighting: Sighting):
	"""
		Insert a sighings object to the database
	"""

	data = sighting.get_data()
	columns = sighting.get_col_names()

	val_str = ['?' for _ in data]

	val_str =  ', '.join(val_str)

	with create_connection(DATABASE) as conn:
		c = conn.cursor()

		query = f"""
			INSERT INTO sightings ({','.join(columns)})
			VALUES ({val_str})
		"""

		try:
			c.execute(query, data)
			conn.commit()
			print("Success")
		except sqlite3.Error as error:
			print(f"Failed to insert.  Error:  {error}")
