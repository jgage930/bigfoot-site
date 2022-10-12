from database.functions import parse_reports
from database.create import insert_sighting

"""Run this file to rebuild data base and insert data from the reports.json"""

def insert_json_data():
	"""Parse json file and insert into database"""

	sightings = parse_reports()

	for sighting in sightings:
		insert_sighting(sighting)

def main():
	insert_json_data()

if __name__ == "__main__":
	main()