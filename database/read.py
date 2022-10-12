from database.setup import create_connection
from database.models import Sighting

DATABASE = '/home/jgage/Documents/Projects/bigfoot-site/database/database.db'

def get_sightings(**kwargs):
	base_query = """
		SELECT * FROM sightings WHERE
	"""
	response = {'sightings': []}
	# we have been given kwargs
	query = base_query

	for key, value in kwargs.items():
		if value is not None:
			query += f"{key} = '{value}'"

		query += "and" if key == 'country' else ';'

	print(kwargs)
	query += ';'

	with create_connection(DATABASE) as conn:
		c = conn.cursor()
		c.execute(query)

		data = c.fetchall()

		for line in data:
			response['sightings'].append(Sighting(*line).to_json())

		return response

def sighings_by_state(state: str):
	query = f"""
		SELECT * FROM sightings Where state = {state};
	"""

	with create_connection(DATABASE) as conn:
		c = conn.cursor()
		c.execute(query)

		data = c.fetchall()
		
		response = {'sightings': []}
		for line in data:
			response['sightings'].append(Sighting(*line).to_json())

		return response