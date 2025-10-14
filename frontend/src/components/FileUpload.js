import React, { useState } from "react";
import { uploadFile } from "../api/api";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return setStatus("⚠️ Please select a PDF file first.");

    try {
      setLoading(true);
      setStatus("Uploading...");
      const res = await uploadFile(file);
      setStatus(`✅ ${res.data.message}`);
    } catch (err) {
      console.error(err);
      setStatus("❌ Upload failed. Please check your backend connection.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h3>📄 Upload PDF Document</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
          disabled={loading}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Uploading..." : "Upload"}
        </button>
      </form>
      <div className="status-message">{status}</div>
    </div>
  );
};

export default FileUpload;
