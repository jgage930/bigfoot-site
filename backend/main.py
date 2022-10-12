from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

## Read Methods ##
from database.read import read_all_sightings, read_sighting

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
def get_sightings(state: str, county: str):
	""" return a list of sightings for a county """
	pass

@app.get('/sightings/{state}')
def get_sightings(state: str):
	""" return a list of sightings ids by state """
	pass