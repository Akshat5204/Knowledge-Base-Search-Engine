import React from "react";

const AnswerDisplay = ({ answer, sources }) => {
  return (
    <div className="card">
      <h3>🧠 Answer</h3>
      <div className="answer-box">
        {answer ? answer : "Ask a question to see the answer here."}
      </div>

      {sources && sources.length > 0 && (
        <div style={{ marginTop: "15px" }}>
          <h4>📑 Relevant Passages</h4>
          <ul>
            {sources.map((s, i) => (
              <li key={i} style={{ marginBottom: "8px" }}>
                {s}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default AnswerDisplay;
