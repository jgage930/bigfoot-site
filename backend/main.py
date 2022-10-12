from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from starlette.middleware.cors import CORSMiddleware

## Read Methods ##
from database.read import (
	read_all_sightings, read_sighting, read_sighting_by_county, read_sightings_by_state, get_county_names
)


app = FastAPI()

# middle ware
# origins = [
# 	'http://localhost:3000',
# 	'http://127.0.0.1:3000'
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

@app.get('/state_data')
def get_state_data():
	""" Return a list of counties by state """
	return get_county_names()