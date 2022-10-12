from database.setup import create_connection, DATABASE
from database.models import Sighting


def read_all_sightings():
	with create_connection(DATABASE) as conn:
		c = conn.cursor()

		query = """
			SELECT * FROM sightings;
		"""

		c.execute(query)

		data = c.fetchall()

	result = {"sightings": []}
	for line in data:
		id, *report = line

		result["sightings"].append(Sighting(*report).to_json())

	return result