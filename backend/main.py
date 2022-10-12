from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/sightings')
def get_sightings():
	""" Returns all sightings as json"""
	pass

@app.get('/sightings/{id}')
def get_sightings(id: int):
	""" Returns sighting by id """
	pass

@app.get('/sightings/{state}/{county}')
def get_sightings(state: str, county: str):
	""" return a list of sightings for a county """
	pass

@app.get('/sightings/{state}')
def get_sightings(state: str):
	""" return a list of sightings ids by state """
	pass