<script setup>
import { ref } from 'vue';
import { ElMessage } from 'element-plus';

const props = defineProps({
  applicantId: {
    type: String,
    required: true
  }
});

const fileInput = ref(null);
const isUploading = ref(false);

const handleFileUpload = async (event) => {
  const file = event.target.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append('file', file);
  formData.append('applicant_id', props.applicantId);

  isUploading.value = true;

  try {
    const response = await fetch('/api/files/upload/', {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      throw new Error('文件上传失败');
    }

    const result = await response.json();
    ElMessage.success('文件上传成功');
  } catch (error) {
    console.error('文件上传错误:', error);
    ElMessage.error(error.message || '文件上传失败');
  } finally {
    isUploading.value = false;
  }
};
</script>

<template>
  <div class="upload-container">
    <div class="upload-box">
      <input
        type="file"
        ref="fileInput"
        @change="handleFileUpload"
        style="display: none"
      />
      <el-button
        :loading="isUploading"
        type="primary"
        @click="fileInput.click()"
      >
        上传文件
      </el-button>
    </div>
  </div>
</template>

<style scoped>
.upload-container {
  padding: 20px;
}

.upload-box {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  border: 2px dashed #dcdfe6;
  border-radius: 8px;
}
</style>