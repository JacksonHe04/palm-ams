import request from '@/utils/http'

export interface FieldItem {
  id: number
  name: string
  description: string
  type: string
  variableName: string
  showInTable: boolean
  showInFilter: boolean
  showInApply: boolean
  showInRecommendMaster: boolean
  showInExamMaster: boolean
  showInPhd: boolean
  showInDirectPhd: boolean
  regionInForm: string
}

// 获取字段列表
export const getFieldList = () => {
  return request.get<FieldItem[]>('/api/field/getFieldList')
}

// 添加字段
export const addField = (data: Omit<FieldItem, 'id'>) => {
  return request.post<FieldItem>('/api/field/addField', data)
}

// 更新字段
export const updateField = (data: FieldItem) => {
  return request.put<FieldItem>(`/api/field/updateField/${data.id}`, data)
}

// 删除字段
export const deleteField = (id: number) => {
  return request.delete(`/api/field/deleteField/${id}`)
}