<template>
  <div class="p-6">
    <el-card>
      <template #header>
        <div class="flex justify-between items-center">
          <div class="flex items-start flex-col">
            <span class="text-xl font-bold">筛选结果</span>
            <div class="text-gray-500 text-sm mt-1">
              查看和导出通过筛选的学生的申请信息
            </div>
          </div>
          <div class="flex gap-2">
            <el-button
              type="primary"
              :loading="downloading"
              @click="downloadAllFiles"
            >
              {{ downloading ? '正在下载...' : '下载所有文件' }}
            </el-button>
            <el-button
              type="success"
              :loading="exporting"
              @click="exportToExcel"
            >
              {{ exporting ? '正在导出...' : '导出Excel' }}
            </el-button>
          </div>
        </div>
      </template>

      <el-tabs v-model="activeTab">
        <el-tab-pane
          v-for="type in applicationTypes"
          :key="type"
          :label="type || '其他'"
          :name="type"
        >
          <student-table
            :data="getStudentsByType(type)"
            :loading="store.loading"
            :column-config="columnConfig"
          />
        </el-tab-pane>
      </el-tabs>

      <!-- 错误提示 -->
      <div v-if="store.error" class="error-message">
        {{ store.error }}
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, computed, watch } from 'vue';
import { useResultStore } from '@/stores/resultStore';
import { useFieldStore } from '@/stores/fieldStore';
import * as XLSX from 'xlsx';
import { ElMessage } from 'element-plus';
import StudentTable from './components/StudentTable.vue';

// 初始化 store
const store = useResultStore();

// 使用 fieldStore
const fieldStore = useFieldStore();

// 获取可展示的字段配置
const columnConfig = computed(() => {
  return fieldStore.fields
    .filter(field => field.showInTable)
    .reduce((acc, field) => {
      acc[field.variableName] = {
        label: field.name,
        width: '150'
      };
      return acc;
    }, {} as Record<string, { label: string; width: string }>);
});

// 在组件挂载时获取字段列表
onMounted(async () => {
  await fieldStore.fetchFields();
  await store.fetchFilteredStudents();
});

// 添加下载状态和下载方法
const downloading = ref(false);
const exporting = ref(false);

async function downloadAllFiles() {
  if (!store.filteredStudents.length) {
    ElMessage.warning('没有可下载的文件');
    return;
  }

  downloading.value = true;
  try {
    const files = store.filteredStudents.filter(student => student.file_path);
    if (!files.length) {
      ElMessage.warning('没有找到可下载的文件');
      return;
    }

    for (const student of files) {
      const url = getFileDownloadUrl(student.file_path);
      const link = document.createElement('a');
      link.href = url;
      link.download = student.file_name || '未命名文件';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      // 添加小延迟，避免浏览器限制
      await new Promise(resolve => setTimeout(resolve, 500));
    }
    ElMessage.success('文件下载完成');
  } catch (error) {
    console.error('下载文件时出错:', error);
    ElMessage.error('下载文件时出错');
  } finally {
    downloading.value = false;
  }
}

// 添加导出Excel方法
async function exportToExcel() {
  if (!store.filteredStudents.length) {
    ElMessage.warning('没有可导出的数据');
    return;
  }

  exporting.value = true;
  try {
    // 准备表格数据
    const exportData = store.filteredStudents.map((student, index) => {
      const row: Record<string, any> = {
        '序号': index + 1
      };
      
      // 添加动态列数据
      Object.entries(columnConfig.value).forEach(([key, config]) => {
        row[config.label] = student[key] === true ? '是' : 
                           student[key] === false ? '否' : 
                           student[key] || '无';
      });

      // 添加论文数据
      row['论文'] = [student.paper1_journalConference, student.paper2_journalConference, student.paper3_journalConference]
        .filter(journal => journal && journal.trim() !== '')
        .join(';') || '无';

      // 添加奖项数据
      row['奖项'] = [student.award1_awardName, student.award2_awardName, student.award3_awardName]
        .filter(award => award && award.trim() !== '')
        .join(';') || '无';

      return row;
    });

    // 创建工作表
    const ws = XLSX.utils.json_to_sheet(exportData);
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, '学生信息');

    // 导出文件
    XLSX.writeFile(wb, `学生信息表_${new Date().toLocaleDateString()}.xlsx`);
    ElMessage.success('导出成功');
  } catch (error) {
    console.error('导出Excel时出错:', error);
    ElMessage.error('导出Excel时出错');
  } finally {
    exporting.value = false;
  }
}

// 添加计算属性来分类学生
// 获取所有申请类型
const applicationTypes = computed(() => {
  const types = new Set(store.filteredStudents.map(student => student.applicationType));
  return Array.from(types);
});

// 根据申请类型获取学生列表
const getStudentsByType = (type: string) => {
  return store.filteredStudents.filter(student => student.applicationType === type);
};

// 添加当前激活的标签页
const activeTab = ref('');

// 监听 applicationTypes 的变化，自动设置第一个标签页
watch(applicationTypes, (types) => {
  if (types.length && !activeTab.value) {
    activeTab.value = types[0];
  }
}, { immediate: true });
</script>

<style lang="scss" scoped>
.el-table {
  --el-table-border-color: #dcdfe6;
  --el-table-header-bg-color: #f5f7fa;

  :deep(th) {
    font-weight: 600;
    color: #606266;
  }
}

.error-message {
  color: #f56c6c;
  margin-top: 10px;
  text-align: center;
}

.el-tabs {
  :deep(.el-tabs__header) {
    margin-bottom: 16px;
  }
}
</style>