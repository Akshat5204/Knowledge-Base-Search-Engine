import axios from "axios";

// Adjust if backend runs on a different port
const API_URL = "http://localhost:5000";

export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  return axios.post(`${API_URL}/upload`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
};

export const askQuestion = async (question) => {
  return axios.post(`${API_URL}/query`, { question });
};
