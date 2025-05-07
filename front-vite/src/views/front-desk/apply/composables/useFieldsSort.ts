import { computed } from 'vue'
import type { FieldItem } from '@/apis/field'

/**
 * 表单字段排序组合式函数
 * @param fields 需要排序的字段数组
 * @returns 排序后的字段数组
 */
export const useFieldsSort = (fields: FieldItem[]) => {
  // 定义区域的显示顺序
  const regionOrder = [
    '个人信息',
    '学历信息',
    '申请志愿',
    '论文情况',
    '奖项',
    '其他'
  ]

  // 定义普通字段的排序顺序
  const normalFieldOrder = [
    'name',
    'gender',
    'birthDate',
    'phone',
    'email',
    'university',
    'major',
    'majorCount',
    'rank',
    'percentage',
    'isTopClass',
    'applicationType',
    'firstChoice',
    'secondChoice',
    'thirdChoice',
    'isAdjustable',
    'year'
  ]

  // 获取普通字段的排序权重
  const getNormalFieldWeight = (variableName: string): number => {
    const index = normalFieldOrder.findIndex(field => variableName === field)
    return index === -1 ? normalFieldOrder.length : index
  }

  // 定义奖项字段的排序顺序
  const awardFieldOrder = ['awardName', 'awardTime', 'levelRanking', 'awardRanking']

  // 获取奖项字段的排序权重
  const getAwardFieldWeight = (variableName: string): number => {
    for (let i = 0; i < awardFieldOrder.length; i++) {
      if (variableName.includes(awardFieldOrder[i])) {
        return i
      }
    }
    return awardFieldOrder.length // 如果不包含任何预定义的字段名，放到最后
  }

  // 对字段进行排序
  const sortedFields = computed(() => {
    return [...fields].sort((a, b) => {
      // 首先按照区域顺序排序
      const regionA = regionOrder.indexOf(a.regionInForm)
      const regionB = regionOrder.indexOf(b.regionInForm)
      if (regionA !== regionB) {
        return regionA - regionB
      }

      // 如果是论文情况，按照论文序号排序
      if (a.regionInForm === '论文情况') {
        const paperNumA = parseInt(a.variableName.match(/paper(\d+)/)?.[1] || '0')
        const paperNumB = parseInt(b.variableName.match(/paper(\d+)/)?.[1] || '0')
        if (paperNumA !== paperNumB) {
          return paperNumA - paperNumB
        }
      }

      // 如果是奖项，先按照奖项序号排序
      if (a.regionInForm === '奖项') {
        const awardNumA = parseInt(a.variableName.match(/award(\d+)/)?.[1] || '0')
        const awardNumB = parseInt(b.variableName.match(/award(\d+)/)?.[1] || '0')
        if (awardNumA !== awardNumB) {
          return awardNumA - awardNumB
        }
        
        // 相同奖项序号的情况下，按照预定义的字段顺序排序
        const weightA = getAwardFieldWeight(a.variableName)
        const weightB = getAwardFieldWeight(b.variableName)
        if (weightA !== weightB) {
          return weightA - weightB
        }
      }

      // 如果是普通字段，按照预定义的字段顺序排序
      const weightA = getNormalFieldWeight(a.variableName)
      const weightB = getNormalFieldWeight(b.variableName)
      if (weightA !== weightB) {
        return weightA - weightB
      }

      // 如果区域相同且不是特殊情况，按照字段名称排序
      return a.name.localeCompare(b.name, 'zh-CN')
    })
  })

  return {
    sortedFields
  }
}