import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { FilterScheme } from '@/apis/filter'
import {
  fetchFilterSchemes,
  createFilterScheme,
  updateFilterScheme,
  deleteFilterScheme,
  toggleFilterScheme
} from '@/apis/filter'
import { ElMessage } from 'element-plus'

export const useFilterStore = defineStore('filter', () => {
  // 筛选方案列表
  const schemes = ref<FilterScheme[]>([])

  // 获取筛选方案列表
  const fetchSchemes = async () => {
    try {
      const response = await fetchFilterSchemes()
      schemes.value = response.data
    } catch (error) {
      ElMessage.error('获取筛选方案失败')
      console.error('获取筛选方案失败:', error)
    }
  }

  // 创建筛选方案
  const createScheme = async (scheme: Omit<FilterScheme, 'id'>) => {
    try {
      const response = await createFilterScheme(scheme)
      schemes.value.push(response.data)
      ElMessage.success('创建筛选方案成功')
      return response.data
    } catch (error) {
      ElMessage.error('创建筛选方案失败')
      console.error('创建筛选方案失败:', error)
      return null
    }
  }

  // 更新筛选方案
  const updateScheme = async (id: number, scheme: Omit<FilterScheme, 'id'>) => {
    try {
      const response = await updateFilterScheme(id, scheme)
      const index = schemes.value.findIndex(s => s.id === id)
      if (index !== -1) {
        schemes.value[index] = response.data
      }
      ElMessage.success('更新筛选方案成功')
      return response.data
    } catch (error) {
      ElMessage.error('更新筛选方案失败')
      console.error('更新筛选方案失败:', error)
      return null
    }
  }

  // 删除筛选方案
  const deleteScheme = async (id: number) => {
    try {
      await deleteFilterScheme(id)
      const index = schemes.value.findIndex(s => s.id === id)
      if (index !== -1) {
        schemes.value.splice(index, 1)
      }
      ElMessage.success('删除筛选方案成功')
      return true
    } catch (error) {
      ElMessage.error('删除筛选方案失败')
      console.error('删除筛选方案失败:', error)
      return false
    }
  }

  // 切换筛选方案启用状态
  const toggleScheme = async (id: number, enabled: boolean) => {
    try {
      await toggleFilterScheme(id, enabled)
      const scheme = schemes.value.find(s => s.id === id)
      if (scheme) {
        scheme.enabled = enabled
      }
      ElMessage.success(`${enabled ? '启用' : '禁用'}筛选方案成功`)
      return true
    } catch (error) {
      ElMessage.error(`${enabled ? '启用' : '禁用'}筛选方案失败`)
      console.error(`${enabled ? '启用' : '禁用'}筛选方案失败:`, error)
      return false
    }
  }

  return {
    schemes,
    fetchSchemes,
    createScheme,
    updateScheme,
    deleteScheme,
    toggleScheme
  }
})