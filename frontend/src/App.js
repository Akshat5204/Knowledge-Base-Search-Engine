import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import QueryInput from "./components/QueryInput";
import AnswerDisplay from "./components/AnswerDisplay";
import "./App.css";

function App() {
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);

  return (
    <div className="app-container">
      <h1>📚 Knowledge Base Search Engine</h1>
      <p className="subtitle">
        Upload your PDFs, then ask any question about their contents.
      </p>

      <FileUpload />
      <QueryInput setAnswer={(a, s) => { setAnswer(a); setSources(s); }} />
      <AnswerDisplay answer={answer} sources={sources} />
    </div>
  );
}

export default App;
