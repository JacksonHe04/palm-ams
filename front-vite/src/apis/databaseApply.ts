import http from '@/utils/http'

/**
 * 数据库申请记录相关的接口
 */

// 定义返回数据的类型
export interface ApplyField {
  name: string
  type: string
  null: boolean
  blank: boolean
  default: any
}

export interface ApplyRecord {
  id: string
  name: string
  applicationType: string
  // ... 其他字段
  [key: string]: any
}

export interface ApplyResponse {
  records: ApplyRecord[]
  fields: ApplyField[]
}

/**
 * 获取所有申请记录和字段信息
 */
export function getAllApplyData() {
  return http.get<ApplyResponse>('/api/database/apply/')
}

/**
 * 创建新的申请记录
 * @param data - 申请记录数据
 */
export function createApplyRecord(data: Partial<ApplyRecord>) {
  return http.post('/api/database/apply/', {
    action: 'create',
    data
  })
}

/**
 * 更新申请记录
 * @param id - 记录ID
 * @param data - 更新的数据
 */
export function updateApplyRecord(id: string, data: Partial<ApplyRecord>) {
  return http.post('/api/database/apply/', {
    action: 'update',
    id,
    data
  })
}

/**
 * 删除申请记录
 * @param id - 要删除的记录ID
 */
export function deleteApplyRecord(id: string) {
  return http.post('/api/database/apply/', {
    action: 'delete',
    id
  })
}