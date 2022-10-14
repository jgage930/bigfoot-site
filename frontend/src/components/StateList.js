
const StateList = (props) => {
	let stateData = props.stateData;

	console.log({stateData});
	return (
		<div className="state-list">
			{stateData.map((stateName) =>(
				<p>{stateName}</p>
			))}
		</div>
	)

}

export default StateList;