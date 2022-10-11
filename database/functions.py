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
	print(df)

get_locations()