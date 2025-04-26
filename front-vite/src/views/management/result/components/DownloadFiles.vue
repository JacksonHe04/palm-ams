<template>
  <el-button
    type="primary"
    :loading="downloading"
    @click="downloadAllFiles"
    :disabled="!hasSelectedStudents && !students.length"
  >
    {{ getButtonText }}
  </el-button>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { ElMessage } from 'element-plus';
import JSZip from 'jszip';
import { getFileDownloadUrl } from '@/apis/files';

// 定义组件的 props
const props = defineProps<{
  students: any[];
  selectedStudents?: any[];
  applicationType: string;
}>();

// 下载状态
const downloading = ref(false);

// 计算是否有选中的学生
const hasSelectedStudents = computed(() => {
  return props.selectedStudents && props.selectedStudents.length > 0;
});

// 计算按钮文本
const getButtonText = computed(() => {
  if (downloading.value) return '正在下载...';
  return hasSelectedStudents.value ? '下载选中学生的文件' : '下载当前表格的所有文件';
});

/**
 * 下载所有文件
 * 将当前标签页中的所有简历文件和证明文件打包下载
 */
async function downloadAllFiles() {
  const targetStudents = hasSelectedStudents.value ? props.selectedStudents : props.students;
  
  if (!targetStudents?.length) {
    ElMessage.warning('没有可下载的文件');
    return;
  }

  downloading.value = true;
  try {
    // 创建 JSZip 实例
    const zip = new JSZip();
    
    // 创建文件夹
    const resumeFolder = zip.folder('证明文件');
    const proofFolder = zip.folder('简历文件');
    
    // 记录已处理的文件，避免重复
    const processedFiles = new Set();
    
    // 处理每个学生的文件
    for (const student of targetStudents) {
      // 处理简历文件
      if (student.resume_file_path && !processedFiles.has(student.resume_file_path)) {
        const url = getFileDownloadUrl(student.resume_file_path);
        if (url) {
          const response = await fetch(url);
          const blob = await response.blob();
          const fileName = student.resume_file_name || `简历_${student.name}_${Date.now()}.pdf`;
          resumeFolder.file(fileName, blob);
          processedFiles.add(student.resume_file_path);
        }
      }
      
      // 处理证明文件
      if (student.proof_file_path && !processedFiles.has(student.proof_file_path)) {
        const url = getFileDownloadUrl(student.proof_file_path);
        if (url) {
          const response = await fetch(url);
          const blob = await response.blob();
          const fileName = student.proof_file_name || `证明_${student.name}_${Date.now()}.pdf`;
          proofFolder.file(fileName, blob);
          processedFiles.add(student.proof_file_path);
        }
      }
    }
    
    // 生成并下载 zip 文件
    const content = await zip.generateAsync({ type: 'blob' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(content);
    link.download = `申请材料_${props.applicationType}_${new Date().toLocaleDateString()}.zip`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(link.href);
    
    ElMessage.success('文件下载完成');
  } catch (error) {
    console.error('下载文件时出错:', error);
    ElMessage.error('下载文件时出错');
  } finally {
    downloading.value = false;
  }
}
</script>