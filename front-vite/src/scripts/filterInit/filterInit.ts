import { createFilterScheme, fetchFilterSchemes, deleteFilterScheme } from '@/apis/filter'
import type { FilterScheme } from '@/apis/filter'

// 预设的筛选方案数据
const presetSchemes: Omit<FilterScheme, 'id'>[] = [
  {
    name: '本科A类前20%',
    enabled: true,
    conditions: [
      { field: '本科等级', operator: '=', value: 'A' },
      { field: '百分比', operator: '<=', value: 20 }
    ]
  },
  {
    name: '本科B类限制专业前20%',
    enabled: true,
    conditions: [
      { field: '本科等级', operator: '=', value: 'B' },
      { field: '百分比', operator: '<=', value: 20 },
      { field: '专业', operator: 'in', value: ['限制专业'] }
    ]
  },
  {
    name: '本科C类限制专业前10%',
    enabled: true,
    conditions: [
      { field: '本科等级', operator: '=', value: 'C' },
      { field: '百分比', operator: '<=', value: 10 },
      { field: '专业', operator: 'in', value: ['限制专业'] }
    ]
  },
  {
    name: '本科B类拔尖班前30%',
    enabled: true,
    conditions: [
      { field: '本科等级', operator: '=', value: 'B' },
      { field: '百分比', operator: '<=', value: 30 },
      { field: '是否为拔尖班', operator: '=', value: '是' }
    ]
  },
  {
    name: '本科C类拔尖班前20%',
    enabled: true,
    conditions: [
      { field: '本科等级', operator: '=', value: 'C' },
      { field: '百分比', operator: '<=', value: 20 },
      { field: '是否为拔尖班', operator: '=', value: '是' }
    ]
  },
  {
    name: '本科B类论文AB前30%',
    enabled: true,
    conditions: [
      { field: '本科等级', operator: '=', value: 'B' },
      { field: '百分比', operator: '<=', value: 30 },
      { field: '论文等级', operator: 'in', value: ['A', 'B'] }
    ]
  },
  {
    name: '本科C类论文AB前20%',
    enabled: true,
    conditions: [
      { field: '本科等级', operator: '=', value: 'C' },
      { field: '百分比', operator: '<=', value: 20 },
      { field: '论文等级', operator: 'in', value: ['A', 'B'] }
    ]
  },
  {
    name: '本科B类竞赛获奖前30%',
    enabled: true,
    conditions: [
      { field: '本科等级', operator: '=', value: 'B' },
      { field: '百分比', operator: '<=', value: 30 },
      { field: '奖项名称', operator: 'in', value: ['挑战杯', '互联网+'] },
      { field: '奖项等级', operator: 'in', value: ['特等奖', '金奖', '一等奖'] }
    ]
  },
  {
    name: '本科C类竞赛获奖前20%',
    enabled: true,
    conditions: [
      { field: '本科等级', operator: '=', value: 'C' },
      { field: '百分比', operator: '<=', value: 20 },
      { field: '奖项名称', operator: 'in', value: ['挑战杯', '互联网+'] },
      { field: '奖项等级', operator: 'in', value: ['特等奖', '金奖', '一等奖'] }
    ]
  }
]

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