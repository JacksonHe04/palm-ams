import { createFilterScheme, fetchFilterSchemes, deleteFilterScheme } from '@/apis/filter'
import type { FilterScheme } from '@/apis/filter'
import presetSchemesData from './filterExamples.json'

// 预设的筛选方案数据
const presetSchemes: Omit<FilterScheme, 'id'>[] = presetSchemesData.map(({ id, ...scheme }) => ({
  ...scheme,
  name: scheme.name
}))


// 初始化函数
export const initializeFilterSchemes = async () => {
  try {
    // 获取所有现有方案
    const response = await fetchFilterSchemes()
    // 删除所有现有方案
    for (const scheme of response.data) {
      await deleteFilterScheme(scheme.id)
    }
    // 依次创建预设方案
    for (const scheme of presetSchemes) {
      await createFilterScheme(scheme)
    }
    return true
  } catch (error) {
    console.error('初始化筛选方案失败:', error)
    return false
  }
}