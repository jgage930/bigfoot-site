import json
from database.models import Sighting

def parse_reports():

	with open(r'/home/jgage/Documents/Projects/bigfoot-site/database/reports.json') as f:
		data = json.load(f)

	report_data = data['reports']

	valid_keys = list(Sighting.__dict__['__annotations__'].keys())
	
	
	sightings = []
	for report in report_data:
		
		valid_keys = list(Sighting.__dict__['__annotations__'].keys())
		sighting_data = report['sighting_data']
		location_data = report['location_data']

		keys_to_add = []

		clean_data = {}

		for key in sighting_data:
			if key in valid_keys:
				clean_data[key] = sighting_data[key]


		clean_data['county'] = location_data['county']
		clean_data['state'] = location_data['state']

		sighting = Sighting(**clean_data)
		sightings.append(sighting)
		
		
	return sightings