import { ref } from 'vue'
import type { Field } from '@/types/field'

export const useFormValidation = () => {
  const requiredFields = ref([
    'name',
    'phone',
    'email',
    'applicationType',
    'university',
    'major',
    'majorCount',
    'rank',
    'year',
  ])

  // 判断字段是否必填
  const isFieldRequired = (fieldName: string) => {
    return requiredFields.value.includes(fieldName)
  }

  // 验证表单数据
  const validateForm = (formData: Record<string, any>, applyFields: Field[]) => {
    for (const fieldName of requiredFields.value) {
      const value = formData[fieldName]
      if (value === undefined || value === '' || (Array.isArray(value) && value.length === 0)) {
        const field = applyFields.find(f => f.variableName === fieldName)
        throw new Error(`${field?.name || fieldName}是必填项`)
      }
    }
    return true
  }

  return {
    requiredFields,
    isFieldRequired,
    validateForm
  }
}