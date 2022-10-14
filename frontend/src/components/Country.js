import { Link } from "react-router-dom";
import {useState, useEffect} from 'react';
import axios from "axios";
import StateList from './StateList';


let Country = () => {
	const [stateData, setStateData] = useState(['no states found']);

	const getData = async () => {
		let res = await axios.get('http://127.0.0.1:8000/state_data');

		let data = res.data;

		setStateData(Object.keys(data));

	}

	useEffect(() => {
		getData()
	}, [])

	return (
		<div className="states">
			<h2>View Sightings by State</h2>
			<StateList stateData={stateData} />

		</div>
	)
}

export default Country;
