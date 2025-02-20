import { defineStore } from 'pinia'
import { ref } from 'vue'
import { submitApplication } from '@/apis/apply'
import { v4 as uuidv4 } from 'uuid'

export const useApplyStore = defineStore('apply', () => {
  // 表单数据
  const formData = ref<Record<string, any>>({})
  
  // 提交状态
  const isSubmitting = ref(false)
  const submitError = ref<string | null>(null)

  // 设置表单数据
  const setFormData = (data: Record<string, any>) => {
    formData.value = data
  }

  // 更新单个字段
  const updateField = (fieldName: string, value: any) => {
    formData.value[fieldName] = value
  }

  // 重置表单
  const resetForm = () => {
    formData.value = {}
    submitError.value = null
  }

  // 提交表单
  const submitForm = async () => {
    isSubmitting.value = true
    submitError.value = null

    try {
      // 在提交前生成并添加 UUID
      const dataWithId = {
        id: uuidv4(),
        ...formData.value
      }
      const response = await submitApplication(dataWithId)
      const responseData = response.data
      resetForm()
      return responseData
    } catch (error: any) {
      submitError.value = error.message || '提交失败，请稍后重试'
      throw error
    } finally {
      isSubmitting.value = false
    }
  }

  return {
    formData,
    isSubmitting,
    submitError,
    setFormData,
    updateField,
    resetForm,
    submitForm
  }
})