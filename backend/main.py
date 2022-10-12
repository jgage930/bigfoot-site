from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from database.read import get_sightings, sighings_by_state

app = FastAPI()

@app.get('/sightings/')
def read_sightings(state: str = None, county: str = None, country:str = "United States"):
	kwargs = {
		"state": state,
		"county": county,
		"country": country
	}
	
	obj = jsonable_encoder(get_sightings(state=state, county=county, country=country))
	return JSONResponse(content=obj)
