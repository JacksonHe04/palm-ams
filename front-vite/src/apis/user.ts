// src/apis/user.js
import http from '@/utils/http';

export const login = (username, password) => {
  return http.post('api/auth/login/', { username, password });
};
