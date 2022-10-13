import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import CarDB from './cardb';
import CarList from './car-list'

ReactDOM.render(
  <React.StrictMode>
    <CarDB />
    <CarList />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA

