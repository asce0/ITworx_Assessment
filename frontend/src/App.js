import React, { useState } from 'react';
import './App.css';

function App() {

  const [ file, setFile ] = useState();

  const newFile = () => {
    const uploadData = new FormData();
    uploadData.append('file', file, file.name);
    
    fetch('http://127.0.0.1:8000/api/analysis/', {
      method: 'POST',
      body: uploadData
    })
    .then( res => console.log(res))
    .catch(error => console.log(error))
  }

  return (
    <div className="App">
      <h3>Upload your File To be processed</h3>
      <label>
        File
        <input type="file" onChange={(evt) => setFile(evt.target.files[0])}/>
      </label>
      <br/>
      <button onClick={() => newFile()}>Upload</button>
    </div>
  );
}

export default App;