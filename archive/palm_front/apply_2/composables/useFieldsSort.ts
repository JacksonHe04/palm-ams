import { computed } from 'vue'
import type { Field } from '@/types/field'

export const useFieldsSort = (fields: Field[]) => {
  const sortedFields = computed(() => {
    // 定义字段组的关键词
    const groups = [
      '论文一',
      '论文二',
      '论文三',
      '奖项一',
      '奖项二',
      '奖项三'
    ]

    // 创建一个Map来存储每个组的字段
    const groupedFields = new Map<string, Field[]>()
    // 创建一个数组来存储不属于任何组的字段
    const otherFields: Field[] = []

    // 初始化分组
    groups.forEach(group => groupedFields.set(group, []))

    // 对字段进行分组
    fields.forEach(field => {
      let matched = false
      for (const group of groups) {
        if (field.name.includes(group)) {
          groupedFields.get(group)?.push(field)
          matched = true
          break
        }
      }
      if (!matched) {
        otherFields.push(field)
      }
    })

    // 合并所有字段
    const result: Field[] = []
    
    // 先添加不属于特定组的字段
    result.push(...otherFields)
    
    // 按顺序添加各组字段
    groups.forEach(group => {
      const groupFields = groupedFields.get(group) || []
      result.push(...groupFields)
    })

    return result
  })

  return {
    sortedFields
  }
}