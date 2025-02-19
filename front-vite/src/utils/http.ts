// src/http.ts
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000',
  // baseURL: 'http://localhost:3000',
  // baseURL: 'http://127.0.0.1:4523/m1/5435287-5110351-default',
  timeout: 10000,
});

// // 添加响应拦截器
// instance.interceptors.response.use(
//   (response) => {
//     // 如果响应数据是对象且有data字段，则返回data字段
//     if (response.data && typeof response.data === 'object') {
//       return response.data.data || response.data;
//     }
//     return response.data;
//   },
//   (error) => {
//     console.error('API请求错误:', error);
//     return Promise.reject(error);
//   }
// );

export default instance;
