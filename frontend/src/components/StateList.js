import { Link } from "react-router-dom";

const StateList = (props) => {
	let stateData = props.stateData;

	console.log({stateData});
	return (
		<div className="state-list">
			{stateData.map((stateName) =>(
				<Link to={'/state_details/' + stateName}>
					<p>{stateName}</p>
				</Link>
			))}
		</div>
	)

}

export default StateList;