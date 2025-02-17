import http from '@/utils/http'

// 筛选方案接口类型定义
export interface FilterScheme {
  id: number
  name: string
  enabled: boolean
  conditions: FilterCondition[]
}

export interface FilterCondition {
  field: string
  operator: string
  value: any
}

// API请求函数
export const fetchFilterSchemes = () => {
  return http.get<FilterScheme[]>('/api/filter/schemes/')
}

export const createFilterScheme = (scheme: Omit<FilterScheme, 'id'>) => {
  return http.post<FilterScheme>('/api/filter/schemes/', scheme)
}

export const updateFilterScheme = (id: number, scheme: Omit<FilterScheme, 'id'>) => {
  return http.put<FilterScheme>(`/api/filter/schemes/${id}/`, scheme)
}

export const deleteFilterScheme = (id: number) => {
  return http.delete(`/api/filter/schemes/${id}/`)
}

export const toggleFilterScheme = (id: number, enabled: boolean) => {
  return http.patch(`/api/filter/schemes/${id}/toggle/`, { enabled })
}