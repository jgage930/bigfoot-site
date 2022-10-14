import axios from "axios";
import React, {useState, useEffect} from 'react';
import { useParams } from "react-router-dom";

function Sighting () {

  const { sighting_id } = useParams();

  const [result, setResult] = useState({'hey': 'yes'});

  const getData = async () => {
    let res = await axios.get('http://127.0.0.1:8000/sightings/' + sighting_id);
    
    let data = res.data;
    let final = data.sightings[0];
    setResult(final)
  }

  useEffect(() =>{
    getData()
  }, [])


  let format = (string) => {
    // Capitilize and remove _ for each string
    string = string.replace('_', ' ');
    return string.charAt(0).toUpperCase() + string.slice(1);
  }

  const header_keys = ['country', 'state', 'county', 'report_id', 'subtitle', 'class_'];

  return(
    <div>
	    
      <span className="locationNav">{result.country} {'>'} {result.state} {">"} {result.county}</span>
		<section className="sightingHeader">
			<span id="title">Report ID #{result.report_id}</span><span id="class">{result.class_}</span>
			<br></br>
			<hr></hr>
			<span id="subtitle">{result.subtitle}</span>
			<hr></hr>
		</section>
		<section className="sightingData">
      {Object.keys(result).map((key) => {
        if (!header_keys.includes(key) && (result[key] != null)) {
          return(
            <div className="entry">
              <h4> {format(key)} </h4> <br></br>
              <span>{result[key]}</span>
            </div>
          )
        }
      })}
		</section>
	</div>
  );
}

export default Sighting;