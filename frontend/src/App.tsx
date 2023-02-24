import React, { useState } from "react";
import "./App.css";

function App() {
  const [meh, setMeh] = useState<number>(1);
  const handleClick = () => setMeh(meh + 1);
  return (
    <div className="App">
      <header className="App-header">
        <p onClick={handleClick}>{meh}</p>
      </header>
    </div>
  );
}

export default App;
