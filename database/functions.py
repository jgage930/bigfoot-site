from models import Location
from typing import List
import pandas as pd

def get_locations() -> List[Location]:
	"""
		parses locationdata.txt and returns a lsit of location objects
	"""

	df = pd.read_csv(
		"location_data.txt",
		sep="|",
		header=None,
		names=["_", "abv", "state", "county", "town"]

	)

	
	location_data = df[["state", "county"]]
	location_data = location_data.drop_duplicates("county")

	locations = []
	id = 1
	for row in location_data.itertuples(index=False):
		state, county = row
		location = Location(id=id, state=state, county=county)
		locations.append(location)

		id += 1

	return locations

def get_sightings():
	"""
	parse sightings and read into a list of objects
	"""