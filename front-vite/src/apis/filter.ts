import http from '@/utils/http'

// 获取所有过滤方案
export const getFilters = () => {
  return http.get('/api/filter/')
}

// 创建新的过滤方案
export const createFilter = (filter) => {
  return http.post('/api/filter/', filter)
}

// 更新过滤方案
export const updateFilter = (filter) => {
  return http.put(`/api/filter/${filter.id}/`, filter)
}

// 删除过滤方案
export const deleteFilter = (filterId) => {
  return http.delete(`/api/filter/${filterId}/`)
}