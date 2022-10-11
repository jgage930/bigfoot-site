import pandas as pd
import requests
from bs4 import BeautifulSoup
import json



def get_span_text(class_: str, soup):
	return soup.find("span", {'class': class_}).text.strip()

def scrape_report(id: int):
	"""
		Scrape a report and format data in the form
		{
			'report_id': ,
			'sighting_data' : [],
			'location_data': [],
			'follow_up_data': []
		}
	"""


	url = f'https://www.bfro.net/GDB/show_report.asp?id={str(id)}'
	r = requests.get(url)

	soup = BeautifulSoup(r.content, 'html.parser')
	# report id
	report_text = get_span_text('reportheader', soup) 

	report_id = report_text[report_text.index("#") + 1: ].strip()

	# class
	class_ = get_span_text('reportheader', soup)

	# find all the span tags in td
	tr = soup.find('tr')

	spans = tr.find_all('span')

	p_tags = tr.find_all('p')

	header_data = []
	content_data = []

	for span in spans:
		header_data.append(span.text.strip())

	for p in p_tags:
		content_data.append(p.text.strip())

	# parse header data
	location_data = header_data[0].split(' > ')

	country = location_data[1]
	state = location_data[2]
	county = location_data[3]

	report_id = location_data[4][location_data[4].index("#") + 1:]

	class_ = header_data[2]

	date_submitted = header_data[3]

	subtitle = header_data[4]

	# parse content_data
	content = {}

	for index, entry in enumerate(content_data):
		data = entry.split(': ')

		if len(data) >= 2:
			key = data[0].lower()

			value = data[1]

			content[key] = value

			last_index = index

	# define the models to return
	sighting = {}
	location = {}
	follow_up = {}

	# sighting
	sighting['report_id'] = report_id
	sighting['class'] = class_
	sighting['date_submitted'] = date_submitted
	sighting['subtitle'] = subtitle

	for key in content:
		sighting[key.replace(' ', '_')] = content[key]

	# location
	location['country'] = country
	location['state'] = state
	location['county'] = county.split(' ')[0]

	# follow_up 
	try:
		follow_up_data = content_data[last_index + 1: ]
		follow_up['title'] = follow_up_data[0]
		follow_up['content'] = follow_up_data[1]
	except:
		print("no follow up")
		
	report = {
		'sighting_data': sighting,
		'location_data': location,
		'follow_up_data': follow_up
	}
	return report

def get_report_ids(state: str, county: str):
	url = f'https://www.bfro.net/GDB/show_county_reports.asp?Show=AB&Submit1=Update&state={state}&county={county}'

	r = requests.get(url)

	soup = BeautifulSoup(r.content, 'html.parser')

	ul = soup.find('ul')

	lis = ul.find_all('li')

	ids = []
	for li in lis:
		span = li.find('span', attrs={'class', 'reportcaption'})
		a = span.find('a')
		href = a.get("href")

		id = href.split('=')[1]
		ids.append(int(id))

	return ids

# read location data into a dataframe
location_data = []
with open('location_data.txt', 'r') as file:
	lines = file.readlines()

	for line in lines:
		line = line.split('|')
		location_data.append(line)


df = pd.DataFrame(
	location_data,
	columns=['City', 'State_Abrev', 'State_Full_Name', 'County', 'Alias']
)

state_abrevs = list(df.State_Abrev.unique())
state_data = {}

for abrev in state_abrevs:

	counties = df.loc[df['State_Abrev'] == abrev].copy()
	counties = list(counties.County.unique())

	state_data[abrev] = counties

# Try to scrap all the sightings data for wi

# scrap all report ids for wi

reports = {"reports": []}
for state in state_abrevs:
	counties = list(map(lambda county: county.title(), state_data[state]))
	print(counties)

	report_ids = []
	for county in counties:
		try:
			report_ids.extend(get_report_ids(state.lower(), county))
		except AttributeError:
			print(f'No Sightings in {county} county')

	for id in report_ids:
		print(f"scraping {str(id)}")

		try:
			reports['reports'].append(scrape_report(id))
		except AttributeError:
			print("no report found")

json_object = json.dumps(reports, indent=4)

with open('reports.json', 'w') as outfile:
	outfile.write(json_object)