import request from '@/utils/http'

/**
 * 获取所有文件数据
 */
export const getAllFilesData = () => {
  return request({
    url: '/api/database/files/',
    method: 'get'
  })
}

/**
 * 创建文件记录
 * @param data 文件数据
 */
export const createFileRecord = (data: any) => {
  return request({
    url: '/api/database/files/',
    method: 'post',
    data: {
      action: 'create',
      data
    }
  })
}

/**
 * 更新文件记录
 * @param id 文件ID
 * @param data 更新的数据
 */
export const updateFileRecord = (id: number, data: any) => {
  return request({
    url: '/api/database/files/',
    method: 'post',
    data: {
      action: 'update',
      id,
      data
    }
  })
}

/**
 * 删除文件记录
 * @param id 文件ID
 */
export const deleteFileRecord = (id: number) => {
  return request({
    url: '/api/database/files/',
    method: 'post',
    data: {
      action: 'delete',
      id
    }
  })
}

// 类型定义
export interface FileField {
  name: string
  type: string
  null: boolean
  blank: boolean
  default: any
}

export interface FileRecord {
  id: number
  applicant_id?: string
  name: string
  original_name: string
  file_path: string
  file_size: number
  file_type: string
  upload_time: string
  uploader?: string
  is_deleted: boolean
  is_resume: boolean
}