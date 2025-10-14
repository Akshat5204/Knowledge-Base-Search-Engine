import React, { useState } from "react";
import { askQuestion } from "../api/api";

const QueryInput = ({ setAnswer }) => {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!question.trim()) return;

    try {
      setLoading(true);
      setStatus("🤔 Thinking...");
      const res = await askQuestion(question);
      if (res.data.answer) {
        setAnswer(res.data.answer, res.data.sources || []);
        setStatus("✅ Answer retrieved!");
      } else {
        setStatus("⚠️ No answer found.");
      }
    } catch (err) {
      console.error(err);
      setStatus("❌ Error fetching answer. Check backend logs.");
      setAnswer("", []);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h3>💡 Ask a Question</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Type your question here..."
          style={{ width: "70%", marginRight: "10px" }}
          disabled={loading}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Thinking..." : "Ask"}
        </button>
      </form>
      <div className="status-message">{status}</div>
    </div>
  );
};

export default QueryInput;
