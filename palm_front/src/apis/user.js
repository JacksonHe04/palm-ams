// src/apis/user.js
import http from '@/utils/http';

export const login = (username, password) => {
  return http.post('/api/login', { username, password });
};

export const register = (username, password) => {
  return http.post('/api/register', { username, password });
};
