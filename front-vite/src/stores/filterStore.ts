import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { createFilter, getFilters, updateFilter, deleteFilter } from '@/apis/filter'

export const useFilterStore = defineStore('filter', () => {
  // 状态
  const savedSchemes = ref([])
  const availableFields = ref([
    { name: 'name', label: '姓名', type: 'string' },
    { name: 'age', label: '年龄', type: 'number' },
    { name: 'university', label: '学校', type: 'string' },
    { name: 'major', label: '专业', type: 'string' },
    { name: 'gpa', label: 'GPA', type: 'number' },
    { name: 'isRecommended', label: '是否推荐', type: 'boolean' }
  ])

  // 方法
  const fetchSchemes = async () => {
    try {
      const response = await getFilters()
      savedSchemes.value = response.data
    } catch (error) {
      console.error('获取过滤方案失败:', error)
      throw error
    }
  }

  const saveScheme = async (scheme) => {
    try {
      const response = await createFilter(scheme)
      savedSchemes.value.push(response.data)
      return response.data
    } catch (error) {
      console.error('保存过滤方案失败:', error)
      throw error
    }
  }

  const updateScheme = async (scheme) => {
    try {
      const response = await updateFilter(scheme)
      const index = savedSchemes.value.findIndex(s => s.id === scheme.id)
      if (index !== -1) {
        savedSchemes.value[index] = response.data
      }
      return response.data
    } catch (error) {
      console.error('更新过滤方案失败:', error)
      throw error
    }
  }

  const removeScheme = async (schemeId) => {
    try {
      await deleteFilter(schemeId)
      const index = savedSchemes.value.findIndex(s => s.id === schemeId)
      if (index !== -1) {
        savedSchemes.value.splice(index, 1)
      }
    } catch (error) {
      console.error('删除过滤方案失败:', error)
      throw error
    }
  }

  return {
    savedSchemes,
    availableFields,
    fetchSchemes,
    saveScheme,
    updateScheme,
    removeScheme
  }
})