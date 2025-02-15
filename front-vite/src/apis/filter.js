// src/apis/filter.js
import http from '@/utils/http';

// 获取所有筛选方案
export function fetchFilterSchemes() {
  return http.get('/api/filter-schemes/');
}

// 保存筛选方案
export function saveFilterScheme(scheme) {
  return http.post('/api/filter-schemes/', scheme);
}

// 更新筛选方案
export function updateFilterScheme(id, scheme) {
  return http.put(`/api/filter-schemes/${id}/`, scheme);
}

// 删除筛选方案
export function deleteFilterScheme(id) {
  return http.delete(`/api/filter-schemes/${id}/`);
}

// 应用筛选方案
export function applyFilterScheme(config) {
  return http.post('/api/filter-schemes/apply/', { config });
}