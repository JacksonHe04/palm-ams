import axios from 'axios';
import type { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios';
import { ElMessage } from 'element-plus';

// 创建 axios 实例
const instance: AxiosInstance = axios.create({
  // baseURL: 'http://localhost:8000', // 开发环境
  // baseURL: 'http://139.155.248.15', // 生产环境
  baseURL: 'https:/palm.inon.space', // 生产环境
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

    // 处理请求重试逻辑
    if (config && retryConfig.retry > 0) {
      // 初始化重试计数器，如果不存在则设为0
      config.__retryCount = config.__retryCount || 0;
      // 判断是否还可以继续重试（当前重试次数小于最大重试次数）
      if (config.__retryCount < retryConfig.retry) {
        // 重试计数器加1
        config.__retryCount++;
        // 延迟指定时间后再次重试，避免频繁请求
        await new Promise(resolve => setTimeout(resolve, retryConfig.retryDelay));
        // 使用 axios 实例重新发起请求
        return instance(config);
      }
    }

    // 错误处理逻辑
    if (response) {
      switch (response.status) {
        case 401:
          ElMessage.error('未授权，请重新登录');
          // 在这里处理登出逻辑
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
