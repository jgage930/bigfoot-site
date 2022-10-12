import React, {useState, useEffect} from 'react'
import axios from 'axios';
import './App.css';


function Sighting () {

  const [result, setResult] = useState({'hey': 'yes'});

  const getData = async () => {
    let res = await axios.get('http://127.0.0.1:8000/sightings/3');
    setResult(res.data);
  }

  useEffect(() =>{
    getData()
  }, [])

  console.log(result);

  return(
    <div>
      <h3>Sighting</h3>
      <p>sighting data</p>
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
