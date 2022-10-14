import axios from "axios";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

function StateDetails () {

	const { state_name } = useParams();
	const [ids, setIds] = useState([1, 2, 3, 4]); 

	const getData = async () => {
		let res = await axios.get('http://127.0.0.1:8000/ids/state/' + state_name);

		let data = res.data['sightings_ids'];
		
		if (data.length < 3) {
			setIds(data);
		} else {
			setIds(data.slice(3));
		}
	}

	useEffect(() => {getData()}, []);

	console.log({ids});

	return (
		<div className="state">
			<h3>{state_name} Sightings</h3>
			<section className="recent">
				{ids.map( (id) => 
					<div>
						<Link to={'/sighting/' + id}>
							{id}
						</Link>
						<br></br>
					</div>
				)}
			</section>

			<section className="counties">

			</section>
		</div>
	)
}

export default StateDetails;