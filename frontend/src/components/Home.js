import { Link } from "react-router-dom";

const Home = () => {
	return (
		<div className="home">
			<section className="header">
				<h2>Welcome to the Bigfoot Sighting Database</h2>
			</section>
			<hr></hr>
			<section className="content">
				<Link to='/usa'>United States</Link>
			</section>
		</div>
	)
}

export default Home;