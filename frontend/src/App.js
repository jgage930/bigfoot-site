import React, {useState, useEffect} from 'react'
import axios from 'axios';
import './App.css';


function Sighting () {

  const [result, setResult] = useState(null);

  const message = async () => {
    try {
      let res = await axios.get("http://127.0.0.1:8000/sightings/98");
      let result = res.data;
      setResult(result);
    } catch(e) {
      console.log('error');
    }
  }

  useEffect( () => {
    message()
  }, [])

  let sightingData = result.sightings[0];
  console.log({sightingData});
  
  return(
    <div>
      <h3>Sighting</h3>
      <p>sighting data</p>

      {Object.keys(sightingData).map((key, index) => {
        return (
          <div key={index}>
            <h2>{key}</h2>
            <br></br>
            <p>{sightingData[key]}</p>
          </div>
        );
      })}
    </div>
  );
}

function App() {
  return (
    <div>
      <Sighting />
    </div>
  
  );
}


export default App;
