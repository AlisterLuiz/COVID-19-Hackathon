import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';
import LatestNews from './Components/LatestNews';

ReactDOM.render(
  <React.StrictMode>
    <LatestNews />
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
