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
  return `${http.defaults.baseURL}${filePath}`
}

// 上传文件的配置
export const uploadConfig = {
  action: `${http.defaults.baseURL}/api/files/upload/`,
  headers: (applicantId: string) => ({
    'X-Applicant-ID': applicantId
  })
}