from dataclasses import dataclass

class Table:
	def get_data(self):
		dict = self.__dict__
		list = [dict[key] for key in dict]
		return tuple(list)

	def get_col_names(self):
		dict = self.__dict__
		return tuple(list(dict))

	def __eq__(self, __o: object) -> bool:
		dict_1 = self.__dict__
		dict_2 = __o.__dict__

		del dict_1['id']
		del dict_2['id']

		print(dict_1)
		print(dict_2)

		return dict_2 == dict_1

@dataclass
class Location(Table):
	id: int
	state: str
	county: str
	country: str = "United States"


	def __eq__(self, __o: object) -> bool:
		dict_1 = self.__dict__
		dict_2 = __o.__dict__

		del dict_1['id']
		del dict_2['id']

		return dict_2 == dict_1

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
