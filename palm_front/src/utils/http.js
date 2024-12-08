// src/http.js
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000',
  timeout: 10000,
});

export function postData(url, data) {
  return instance.post(url, data)
    .then(response => response.data)
    .catch(error => {
      console.error('There was an error!', error);
      throw error;
    });
}

export default instance;
