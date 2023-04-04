import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [songs, setSongs] = useState([]);

  useEffect(() => {
    fetch('/api/songs')
      .then(res => res.json())
      .then(data => setSongs(data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div className="App">
      <h1>My Spotify Clone</h1>
      <ul>
        {songs.map(song => (
          <li key={song.title}>
            {song.title} by {song.artist} ({song.album})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
