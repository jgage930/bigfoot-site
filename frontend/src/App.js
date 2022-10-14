// other packages
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import axios from 'axios';
import './App.css';
// components
import Home from './components/Home';
import Country from './components/Country';
import StateDetails from './components/StateDetails';
import Sighting from './components/Sighting';


function App() {
  return (
    <Router>
      <div className='App'>
        <div className='content'>
          <Switch>

            <Route exact path='/'>
              <Home />
            </Route>

            <Route path='/usa'>
              <Country />
            </Route>

            <Route path="/state_details/:state_name">
              <StateDetails />
            </Route>

            <Route path="/sighting/:sighting_id">
              <Sighting />
            </Route>

          </Switch>
        </div>
      </div>

    </Router>
  );
}


export default App;
