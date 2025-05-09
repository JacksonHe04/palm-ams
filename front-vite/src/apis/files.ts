import http from '@/utils/http'

export interface FileItem {
  id: number
  name: string
  file_type: string
  upload_time: string
  file_path: string
}

// 获取文件列表
export const getFileList = (applicantId: string) => {
  return http.get<FileItem[]>(`/api/files`, {
    params: {
      applicant_id: applicantId
    }
  })
}

// 删除文件
export const deleteFile = (fileId: number) => {
  return http.delete(`/api/files/${fileId}`)
}

// 获取文件下载链接
export const getFileDownloadUrl = (filePath: string) => {
  // 如果路径以 /api/files/download/ 开头，直接返回完整URL
  if (filePath.startsWith('/api/files/download/')) {
    return `${http.defaults.baseURL}${filePath}`
  }
  return null
}

// 上传文件的配置
export const uploadConfig = {
  action: `${http.defaults.baseURL}/api/files/upload/`,
  headers: (applicantId: string) => ({
    'X-Applicant-ID': applicantId
  })
}

// 上传简历的配置
export const resumeUploadConfig = {
  action: `${http.defaults.baseURL}/api/files/upload-resume/`,
  headers: (applicantId: string) => ({
    'X-Applicant-ID': applicantId
  })
}

/**
 * 批量下载文件
 * @param fileIds 文件ID列表
 * @param applicationType 申请类型
 * @returns 文件流
 */
export const batchDownloadFiles = (fileIds: number[], applicationType: string) => {
  return http.post('/api/files/batch-download/', {
    file_ids: fileIds,
    application_type: applicationType
  }, {
    responseType: 'blob',
    timeout: 180000  // 设置180秒超时时间
  })
}