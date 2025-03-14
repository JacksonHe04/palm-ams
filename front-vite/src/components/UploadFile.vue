<template>
  <div class="upload-container">
    <el-upload
      class="upload-area"
      :action="uploadConfig.action"
      :headers="headers"
      :on-success="handleUploadSuccess"
      :on-error="handleUploadError"
      :before-upload="beforeUpload"
      multiple
    >
      <el-button type="primary">上传证明材料</el-button>
      <template #tip>
        <div class="el-upload__tip">
          请上传ZIP格式的压缩文件，文件大小不超过100MB
        </div>
      </template>
    </el-upload>

    <div v-if="fileList.length > 0" class="file-list">
      <h3>已上传文件：</h3>
      <el-table :data="fileList" style="width: 100%">
        <el-table-column prop="name" label="文件名" />
        <el-table-column prop="file_type" label="类型" width="100" />
        <el-table-column prop="upload_time" label="上传时间" width="180" />
        <el-table-column fixed="right" label="操作" width="100">
          <template #default="scope">
            <el-button
              type="danger"
              size="small"
              @click="handleDelete(scope.row)"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { ElMessage } from 'element-plus'
import type { UploadProps } from 'element-plus'
import { useApplyStore } from '@/stores/applyStore'
import { getFileList, deleteFile, uploadConfig, type FileItem } from '@/apis/files'

const fileList = ref<FileItem[]>([])
const applyStore = useApplyStore()

// 从pinia store获取applicantId
const applicantId = computed(() => applyStore.formData.id)

// 计算上传请求头
const headers = computed(() => uploadConfig.headers(applicantId.value))

// 上传前的验证
const beforeUpload: UploadProps['beforeUpload'] = (file) => {
  const isValidType = ['application/zip', 'application/x-zip-compressed'].includes(file.type)
  if (!isValidType) {
    ElMessage.error('只能上传ZIP格式的文件！')
    return false
  }
  const isLt100M = file.size / 1024 / 1024 < 100
  if (!isLt100M) {
    ElMessage.error('文件大小不能超过100MB！')
    return false
  }
  return true
}

// 上传成功的回调
const handleUploadSuccess = (response: any) => {
  ElMessage.success('文件上传成功')
  fetchFileList()
  applyStore.updateField('proofs', response.file_path)
}

// 上传失败的回调
const handleUploadError = () => {
  ElMessage.error('文件上传失败，请重试')
}

// 删除文件
const handleDelete = async (file: FileItem) => {
  try {
    await deleteFile(file.id)
    ElMessage.success('文件删除成功')
    fetchFileList()
  } catch (error) {
    ElMessage.error('文件删除失败，请重试')
  }
}

// 获取已上传的文件列表
const fetchFileList = async () => {
  try {
    const { data } = await getFileList(applicantId.value)
    fileList.value = data
  } catch (error: any) {
    console.error('获取文件列表失败：', error.message)
  }
}

onMounted(() => {
  if (applicantId.value) {
    fetchFileList()
  }
})
</script>

<style scoped>
.upload-container {
  margin: 20px 0;
  padding: 20px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
}

.upload-area {
  margin-bottom: 20px;
}

.file-list {
  margin-top: 20px;
}

.el-upload__tip {
  color: #666;
  font-size: 14px;
  margin-top: 8px;
}
</style>