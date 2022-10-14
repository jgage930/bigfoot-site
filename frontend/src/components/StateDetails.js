import { useParams } from "react-router-dom";

function StateDetails () {

	const { state_name } = useParams()

	return (
		<div className="state">
			<h3>{state_name} Sightings</h3>
		</div>
	)
}

export default StateDetails;