import React from 'react';
import './App.css';
import frontpageImage from './assets/images/frontpage.png';

function App() {
  return (
    <div className="app">
      <img src={frontpageImage} alt="Background" className="background-image" />
    </div>
  );
}

export default App;