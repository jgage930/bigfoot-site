from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

## Read Methods ##
from database.read import read_all_sightings, read_sighting, read_sighting_by_county, read_sightings_by_state

app = FastAPI()

@app.get('/sightings')
def get_sightings(limit: int):
	""" Returns all sightings as json"""
	obj = jsonable_encoder(read_all_sightings(limit=limit))
	return JSONResponse(content=obj)
	

@app.get('/sightings/{id}')
def get_sightings(id: int):
	""" Returns sighting by id """
	obj = jsonable_encoder(read_sighting(id))
	return JSONResponse(content=obj)

@app.get('/sightings/{state}/{county}')
def get_sightings_by_county(state: str, county: str):
	""" return a list of sightings for a county """
	obj = jsonable_encoder(read_sighting_by_county(state, county))
	return JSONResponse(content=obj)

@app.get('/ids/state/{state}')
def get_sightings_by_state(state: str):
	""" return a list of sightings ids by state """

	obj = jsonable_encoder(read_sightings_by_state(state))
	return JSONResponse(content=obj)