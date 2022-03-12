import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";

import Login from '../login/login';
import Header from '../header/header';
import Dashboard from '../dashboard/dashboard';
import Preferences from '../preferences/preferences';
var session = require("../../services/session/session");

export default class App extends React.Component{
  constructor(props) {
    super(props);
    this.handleLoginChange = this.handleLoginChange.bind(this);
    this.refreshSessionToken = this.refreshSessionToken.bind(this);
    this.state = {
      logged: false,
    }
  }

  componentDidMount() {
    this.timerID = setInterval(
      () => this.refreshSessionToken(),
      60000
    );
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  refreshSessionToken() {
    session.refresh();
  }

  handleLoginChange(newState) {
    this.setState({logged: newState});
  }

  render() {
    if (! this.state.logged) {
      return (
        <Login handleLoginChange={this.handleLoginChange} />
      )
    }
    return (
      <div className="main">
        <Header handleLoginChange={this.handleLoginChange} />
        <Router>
          <div>
            <ul>
              <li>
                <Link to="/preferences">Preferences</Link>
              </li>
              <li>
                <Link to="/dashboard">Dashboard</Link>
              </li>
            </ul>
            <Routes>
              <Route exact path="/preferences" element={<Preferences/>}/>
              <Route exact path="/dashboard" element={<Dashboard/>}/>
            </Routes>
          </div>
        </Router>
      </div>
    );
  }
}
