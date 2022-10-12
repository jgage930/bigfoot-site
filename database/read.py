from database.setup import create_connection, DATABASE
from database.models import Sighting
import pandas as pd


def read_all_sightings(limit: int):
	with create_connection(DATABASE) as conn:
		c = conn.cursor()

		query = f"""
			SELECT * FROM sightings
			LIMIT {limit};
		"""

		c.execute(query)

		data = c.fetchall()

	result = {
		"sightings": []
		}
	for line in data:
		id, *report = line

		result["sightings"].append(Sighting(*report).to_json())

	return result

def read_sighting(id: int):
	with create_connection(DATABASE) as conn:
		c = conn.cursor()

		query = f"""
			SELECT * FROM sightings
			WHERE id = {id};
		"""

		c.execute(query)
		data = c.fetchall()

		
	result = {"id": id, "sightings": []}
	for line in data:
		id, *report = line

		result["sightings"].append(Sighting(*report).to_json())

	return result

def read_sighting_by_county(state: str, county: str):
	with create_connection(DATABASE) as conn:
		c = conn.cursor()

		query = f"""
			SELECT * FROM sightings
			WHERE state = '{state}' and county = '{county}';
		"""

		c.execute(query)
		data = c.fetchall()

	result = {"sightings": []}
	for line in data:
		id, *report = line

		result["sightings"].append(Sighting(*report).to_json())

	return result

def read_sightings_by_state(state: str):
	with create_connection(DATABASE) as conn:
		c = conn.cursor()

		query = f"""
			SELECT id FROM sightings
			WHERE state = '{state}';
		"""

		c.execute(query)
		data = c.fetchall()

	result = {"sightings_ids": []}
	for line in data:
		id, = line
		result["sightings_ids"].append(id)

	return result

def get_county_names():
	""" returns a dictionary in form 
		{
			"state_name" : 
				{
					"counties": []
				}
		}
	"""

	result = {}

	file_name = r'/home/jgage/Documents/Projects/bigfoot-site/database/location_data.txt'
	df = pd.read_csv(
		file_name,
		header=None,
		sep='|',
		names = ['township', 'abbrev', 'state', 'county', 'town']
	)

	sub = df[['state', 'county']]
	sub = sub.drop_duplicates()

	# get list of state names
	state_names = list(pd.unique(sub['state']))
	
	# format dict
	county_groups = sub.groupby('state')
	
	for name in state_names:
		county_names = []
		group = county_groups.get_group(name)


		for index, row in group.iterrows():
			county = str(row['county'])
			county_names.append(county)

		result[name] = county_names 

	return result