import { Link } from "react-router-dom";

const CountyList = (props) => {
	let countyData = props.countyData;

	return (
		<div className="county-list">
			{countyData.map( (countyName) => 
				<Link to={'/'}>
					{countyName}
				</Link>	
			)}
		</div>
	)

}