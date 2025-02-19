import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Apply } from '@/apis/apply'
import { processFilters } from '@/apis/filter_processor'

export const useFilterProcessorStore = defineStore('filterProcessor', () => {
  // 存储筛选后的申请记录
  const filteredApplies = ref<Apply[]>([])
  
  // 执行筛选并更新状态
  const executeFilters = async () => {
    try {
      const result = await processFilters()
      filteredApplies.value = result
      return result
    } catch (error) {
      console.error('执行筛选失败:', error)
      throw error
    }
  }

  return {
    filteredApplies,
    executeFilters
  }
})