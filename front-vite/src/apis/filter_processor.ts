import http from '@/utils/http'
import type { Apply } from './apply'

// 执行筛选方案的API请求函数
export const processFilters = () => {
  return http.get<Apply[]>('/api/filter/process/')
}