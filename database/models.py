from dataclasses import dataclass

class Table:
	def get_data(self):
		dict = self.__dict__
		list = [dict[key] for key in dict]
		return tuple(list)

	def get_col_names(self):
		dict = self.__dict__
		return tuple(list(dict))


@dataclass
class Location(Table):
	id: int
	country: str
	state: str
	county: str

@dataclass
class FollowUp(Table):
	id: int
	title: str
	content: str

@dataclass
class Sighting(Table):
	
	id: int 
	report_id: str
	class_: str
	date_submitted: str
	subtitle: str
	year: str
	season: str
	month : str
	date : str
	nearest_town : str
	nearest_road : str
	observed: str
	also_noticed : str
	other_witnesses: str
	other_stories: str
	time_and_conditions: str
	environment: str
	misc: str
	location_id: id
	follow_up_id: id
