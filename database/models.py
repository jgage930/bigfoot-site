from dataclasses import dataclass

@dataclass
class Sighting:
	report_id: str = None
	class_: str = None
	date_submitted: str = None
	subtitle: str = None
	year: str = None
	season: str = None
	month : str = None
	date : str = None
	location_details: str = None
	nearest_town : str = None
	nearest_road : str = None
	observed: str = None
	also_noticed : str = None
	other_witnesses: str = None
	other_stories: str = None
	time_and_conditions: str = None
	environment: str = None
	county:str = None
	state: str = None
	country: str = "United States"

	def get_data(self):
		return tuple(self.__dict__.values())

	def get_col_names(self):
		return tuple(self.__dict__.keys())

	def to_json(self) -> dict:
		return self.__dict__