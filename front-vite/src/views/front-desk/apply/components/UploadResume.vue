<template>
  <div class="upload-container">
    <el-upload
      class="upload-area"
      :action="resumeUploadConfig.action"
      :headers="headers"
      :on-success="handleUploadSuccess"
      :on-error="handleUploadError"
      :before-upload="beforeUpload"
      :limit="1"
      :auto-upload="true"
    >
      <el-button type="primary">上传简历</el-button>
      <template #tip>
        <div class="el-upload__tip">
          请上传PDF格式的简历文件，文件大小不超过10MB<br>
          请将简历命名为：学校-姓名-简历.pdf<br>
          示例：东南大学-小明-简历.pdf
        </div>
      </template>
    </el-upload>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { ElMessage } from 'element-plus'
import type { UploadProps } from 'element-plus'
import { useApplyStore } from '@/stores/applyStore'
import { resumeUploadConfig } from '@/apis/files'

const applyStore = useApplyStore()

// 从pinia store获取applicantId
const applicantId = computed(() => applyStore.formData.id)

// 计算上传请求头
const headers = computed(() => resumeUploadConfig.headers(applicantId.value))

// 上传前的验证
const beforeUpload: UploadProps['beforeUpload'] = (file) => {
  const isValidType = file.type === 'application/pdf'
  if (!isValidType) {
    ElMessage.error('只能上传PDF格式的文件！')
    return false
  }
  const isLt10M = file.size / 1024 / 1024 < 10
  if (!isLt10M) {
    ElMessage.error('文件大小不能超过10MB！')
    return false
  }
  
  // 新增文件名验证逻辑
  const fileName = file.name.split('.')[0] // 去掉后缀
  if (!fileName.endsWith('-简历')) {
    ElMessage.error('文件名格式不正确，请按照"学校-姓名-简历.pdf"格式命名')
    return false
  }
  
  return true
}

// 上传成功的回调
const handleUploadSuccess = (response: any) => {
  ElMessage.success('简历上传成功')
  applyStore.updateField('resume', response.file_path)
}

// 上传失败的回调
const handleUploadError = () => {
  ElMessage.error('简历上传失败，请重试')
}
</script>

<style scoped>
.upload-container {
  margin: 20px 0;
  padding: 20px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
}

/* .upload-area {
  /* margin-bottom: 20px; */
/* } */

.el-upload__tip {
  color: #666;
  font-size: 14px;
  margin-top: 8px;
}
</style>