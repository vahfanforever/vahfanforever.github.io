import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState('');

  useEffect(() => {
    // Fetch data from the backend when the component mounts
    axios.get('/api/data').then((response) => {
      setData(response.data.message);
    });
  }, []);

  return (
    <div className="App">
      <h1>Static Website with React and Python</h1>
      <p>Data from the backend: {data}</p>
    </div>
  );
}

export default App;