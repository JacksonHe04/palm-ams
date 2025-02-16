import { defineStore } from 'pinia'
import { ref } from 'vue'
import { FieldItem, getFieldList, addField, updateField, deleteField } from '@/apis/field'
import { ElMessage } from 'element-plus'

export const useFieldStore = defineStore('field', () => {
  // 字段列表
  const fields = ref<FieldItem[]>([])

  // 获取字段列表
  const fetchFields = async () => {
    try {
      const response = await getFieldList()
      fields.value = response.data
    } catch (error) {
      ElMessage.error('获取字段列表失败')
      console.error('获取字段列表失败:', error)
    }
  }

  // 添加字段
  const createField = async (fieldData: Omit<FieldItem, 'id'>) => {
    try {
      const response = await addField(fieldData)
      fields.value.push(response)
      ElMessage.success('添加成功')
      return true
    } catch (error) {
      ElMessage.error('添加失败')
      console.error('添加字段失败:', error)
      return false
    }
  }

  // 更新字段
  const editField = async (fieldData: FieldItem) => {
    try {
      const response = await updateField(fieldData)
      const index = fields.value.findIndex(item => item.id === fieldData.id)
      if (index !== -1) {
        fields.value[index] = response
      }
      ElMessage.success('修改成功')
      return true
    } catch (error) {
      ElMessage.error('修改失败')
      console.error('更新字段失败:', error)
      return false
    }
  }

  // 删除字段
  const removeField = async (id: number) => {
    try {
      await deleteField(id)
      const index = fields.value.findIndex(item => item.id === id)
      if (index !== -1) {
        fields.value.splice(index, 1)
      }
      ElMessage.success('删除成功')
      return true
    } catch (error) {
      ElMessage.error('删除失败')
      console.error('删除字段失败:', error)
      return false
    }
  }

  return {
    fields,
    fetchFields,
    createField,
    editField,
    removeField
  }
})