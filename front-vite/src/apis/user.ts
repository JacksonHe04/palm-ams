// src/apis/user.js
import http from '@/utils/http';

export const login = (username, password) => {
  return http.post('api/auth/login/', { username, password });
};

export const getUserInfo = () => {
  const token = localStorage.getItem('token');
  return http.get('api/auth/user_info/', {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
};

export const updateUserInfo = (data) => {
  const token = localStorage.getItem('token');
  return http.put('api/auth/user_info/', data, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
};
