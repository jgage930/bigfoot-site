// other packages
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import axios from 'axios';
import './App.css';
// components
import Home from './components/Home';
import Country from './components/Country';


function App() {
  return (
    <Router>
      <div className='App'>
        <div className='content'>
          <Switch>
            <Route exact path='/'>
              <Home />
            </Route>
            <Route exact path='/usa'>
              <Country />
            </Route>
          </Switch>
        </div>
      </div>

    </Router>
  );
}


export default App;
