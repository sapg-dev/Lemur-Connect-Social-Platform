import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
// Import the axios module
const axios = require('axios');


axios.defaults.baseURL = 'https://lemurconnect.pacifictrout.com';


ReactDOM.render(<App />, document.getElementById('root'));
