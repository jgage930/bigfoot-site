import React, {useState, useEffect} from 'react'
import axios from 'axios';
import './App.css';


function Sighting () {

  const [result, setResult] = useState({'hey': 'yes'});

  const getData = async () => {
    let res = await axios.get('http://127.0.0.1:8000/sightings/3');
    
    let data = res.data;
    let final = data.sightings[0];
    setResult(final)
  }

  useEffect(() =>{
    getData()
  }, [])

  
  return(
    <div>
      <h3>Sighting</h3>
      <p>sighting data</p>
      {Object.keys(result).map((key, index) => {
        return (
          <div>
            <h2>{key}</h2>
            <p>{result[key]}</p>
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
