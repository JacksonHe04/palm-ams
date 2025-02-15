import { defineStore } from 'pinia'
import { ref } from 'vue'
import { fetchFilterSchemes, saveFilterScheme, updateFilterScheme, deleteFilterScheme, applyFilterScheme } from '@/apis/filter'

export const useFilterStore = defineStore('filter', () => {
  const availableFields = ref([
    { name: 'id', label: 'ID', type: 'number' },
    { name: 'name', label: '姓名', type: 'string' },
    { name: 'applicationType', label: '报名类型', type: 'string' },
    { name: 'graduationYear', label: '毕业年份', type: 'number' },
    { name: 'gender', label: '性别', type: 'string' },
    { name: 'birthDate', label: '出生年月', type: 'string' },
    { name: 'photo', label: '照片', type: 'string' },
    { name: 'university', label: '本科学校', type: 'string' },
    { name: 'universityLevel', label: '本科等级', type: 'string' },
    { name: 'major', label: '本科专业', type: 'string' },
    { name: 'majorCount', label: '专业人数', type: 'number' },
    { name: 'rank', label: '排名', type: 'number' },
    { name: 'percentage', label: '百分比', type: 'number' },
    { name: 'masterUniversity', label: '硕士学校', type: 'string' },
    { name: 'masterUniversityLevel', label: '硕士等级', type: 'string' },
    { name: 'masterMajor', label: '硕士专业', type: 'string' },
    { name: 'tutor', label: '导师', type: 'string' },
    { name: 'phone', label: '手机号码', type: 'string' },
    { name: 'email', label: '电子邮箱', type: 'string' },
    { name: 'firstChoice', label: '第一志愿', type: 'string' },
    { name: 'secondChoice', label: '第二志愿', type: 'string' },
    { name: 'thirdChoice', label: '第三志愿', type: 'string' },
    { name: 'isAdjustable', label: '是否服从调剂', type: 'boolean' },
    { name: 'resume', label: '简历文件', type: 'string' },
    { name: 'proofs', label: '证明材料', type: 'string' },
    { name: 'status', label: '状态', type: 'string' }
  ])

  const savedSchemes = ref([])

  // 获取所有筛选方案
  const fetchSchemes = async () => {
    try {
      const response = await fetchFilterSchemes()
      savedSchemes.value = response.data
    } catch (error) {
      console.error('获取筛选方案失败:', error)
      throw error
    }
  }

  // 保存筛选方案
  const saveScheme = async (scheme) => {
    try {
      const response = await saveFilterScheme(scheme)
      savedSchemes.value.push(response.data)
      return response.data
    } catch (error) {
      console.error('保存筛选方案失败:', error)
      throw error
    }
  }

  // 更新筛选方案
  const updateScheme = async (id, scheme) => {
    try {
      const response = await updateFilterScheme(id, scheme)
      const index = savedSchemes.value.findIndex(s => s.id === id)
      if (index !== -1) {
        savedSchemes.value[index] = response.data
      }
      return response.data
    } catch (error) {
      console.error('更新筛选方案失败:', error)
      throw error
    }
  }

  // 删除筛选方案
  const deleteScheme = async (id) => {
    try {
      await deleteFilterScheme(id)
      const index = savedSchemes.value.findIndex(s => s.id === id)
      if (index !== -1) {
        savedSchemes.value.splice(index, 1)
      }
    } catch (error) {
      console.error('删除筛选方案失败:', error)
      throw error
    }
  }

  // 应用筛选方案
  const applyFilter = async (config) => {
    try {
      const response = await applyFilterScheme(config)
      return response.data
    } catch (error) {
      console.error('应用筛选方案失败:', error)
      throw error
    }
  }

  return {
    availableFields,
    savedSchemes,
    fetchSchemes,
    saveScheme,
    updateScheme,
    deleteScheme,
    applyFilter
  }
})