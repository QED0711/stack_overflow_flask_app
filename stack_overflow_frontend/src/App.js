import React, { useState } from 'react';

import './App.css';


import UserForm from './components/UserForm';

const App = () => {
  const [prediction, setPrediction] = useState("")
  
  return (
    <div className="App">
      <UserForm setPrediction={setPrediction} />
      <h1>{prediction}</h1>
    </div>
  );
}

export default App;
