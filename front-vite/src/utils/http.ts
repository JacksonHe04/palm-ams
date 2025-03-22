import axios from 'axios';
import type { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios';
import { ElMessage } from 'element-plus';

// 创建 axios 实例
const instance: AxiosInstance = axios.create({
  baseURL: 'http://localhost:8000',
  timeout: 10000,
});

// 请求重试配置
const retryConfig = {
  retry: 2, // 重试次数
  retryDelay: 1000, // 重试间隔
};

// 请求拦截器
instance.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    // 获取并注入 token
    const token = localStorage.getItem('token');
    if (token) {
      config.headers = {
        ...config.headers,
        Authorization: `Bearer ${token}`,
      };
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 响应拦截器
instance.interceptors.response.use(
  (response: AxiosResponse) => {
    // 如果响应本身就是数据对象，直接返回
    if (response.data && !response.data.data) {
      return {
        data: response.data
      };
    }
    // 如果响应包含 data 字段，保持原样返回
    return response.data;
  },
  async (error) => {
    const { config, response } = error;

    // 处理重试逻辑保持不变
    if (config && retryConfig.retry > 0) {
      config.__retryCount = config.__retryCount || 0;
      if (config.__retryCount < retryConfig.retry) {
        config.__retryCount++;
        await new Promise(resolve => setTimeout(resolve, retryConfig.retryDelay));
        return instance(config);
      }
    }

    // 错误处理逻辑保持不变
    if (response) {
      switch (response.status) {
        case 401:
          ElMessage.error('未授权，请重新登录');
          // 可以在这里处理登出逻辑
          localStorage.removeItem('token');
          window.location.href = '/login';
          break;
        case 403:
          ElMessage.error('拒绝访问');
          break;
        case 404:
          ElMessage.error('请求的资源不存在');
          break;
        case 500:
          ElMessage.error('服务器错误');
          break;
        default:
          ElMessage.error(response.data?.message || '请求失败');
      }
    } else {
      ElMessage.error('网络错误，请检查网络连接');
    }

    return Promise.reject(error);
  }
);

export default instance;
