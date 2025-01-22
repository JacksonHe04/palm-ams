// src/http.js
import axios from 'axios';

const instance = axios.create({
  // baseURL: 'http://localhost:8000',
  baseURL: 'http://localhost:3000',
  // baseURL: 'http://127.0.0.1:4523/m1/5435287-5110351-default',
  timeout: 10000,

});

export default instance;
