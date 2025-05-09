<template>
  <div>
    <el-button
      type="primary"
      :loading="downloading"
      @click="downloadAllFiles"
      :disabled="!hasSelectedStudents && !students.length"
    >
      {{ getButtonText }}
    </el-button>
    
    <!-- 添加进度条对话框 -->
    <el-dialog
      v-model="showProgress"
      title="文件下载中"
      :close-on-click-modal="false"
      :close-on-press-escape="false"
      :show-close="false"
      width="30%"
    >
      <el-progress
        :percentage="downloadProgress"
        :format="progressFormat"
        status="success"
      />
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { ElMessage } from 'element-plus';
import { batchDownloadFiles } from '@/apis/files';

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

// 下载进度相关
const showProgress = ref(false);
const downloadProgress = ref(0);

// 格式化进度显示
const progressFormat = (percentage: number) => {
  return percentage === 100 ? '打包完成' : `${percentage}%`;
};

// 监听下载进度事件
const handleDownloadProgress = (event: CustomEvent) => {
  downloadProgress.value = event.detail;
};

// 组件挂载时添加事件监听
onMounted(() => {
  window.addEventListener('download-progress', handleDownloadProgress as EventListener);
});

// 组件卸载时移除事件监听
onUnmounted(() => {
  window.removeEventListener('download-progress', handleDownloadProgress as EventListener);
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
  showProgress.value = true;
  downloadProgress.value = 0;
  
  try {
    // 收集所有文件ID
    const fileIds = new Set<number>();
    for (const student of targetStudents) {
      if (student.resume_file_path) {
        // 从路径中提取ID，例如从 "/api/files/download/21" 提取 "21"
        const resumeId = parseInt(student.resume_file_path.split('/').pop() || '');
        if (!isNaN(resumeId)) {
          fileIds.add(resumeId);
        }
      }
      if (student.proof_file_path) {
        const proofId = parseInt(student.proof_file_path.split('/').pop() || '');
        if (!isNaN(proofId)) {
          fileIds.add(proofId);
        }
      }
    }

    // 检查是否有可下载的文件
    if (fileIds.size === 0) {
      ElMessage.warning('所选学生没有上传任何文件');
      return;
    }

    // 调用后端批量下载接口
    const response = await batchDownloadFiles(Array.from(fileIds), props.applicationType);
    
    // 创建下载链接
    const blob = new Blob([response.data], { type: 'application/zip' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
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
    showProgress.value = false;
    downloadProgress.value = 0;
  }
}
</script>