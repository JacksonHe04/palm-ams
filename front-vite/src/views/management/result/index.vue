<template>
  <div class="result-table">
    <!-- 添加批量下载按钮和导出Excel按钮 -->
    <div class="mb-4 flex gap-2">
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

    <el-table
      v-loading="store.loading"
      :data="store.filteredStudents"
      style="width: 100%"
      border
      :table-layout="'auto'"
    >
      <!-- 序号列 -->
      <el-table-column type="index" label="#" width="50" />

      <!-- 动态生成列 -->
      <el-table-column
        v-for="(value, key) in columnConfig"
        :key="key"
        :prop="key"
        :label="value.label"
        :min-width="value.width"
      >
        <template #default="scope">
          <template v-if="scope.row[key] === true || scope.row[key] === false">
            {{ scope.row[key] ? '是' : '否' }}
          </template>
          <template v-else>
            {{ scope.row[key] || '无' }}
          </template>
        </template>
      </el-table-column>
      
      <!-- 论文列 -->
      <el-table-column
        label="论文"
        min-width="80"
      >
        <template #default="scope">
          {{ [scope.row.paper1_journalConference, scope.row.paper2_journalConference, scope.row.paper3_journalConference]
              .filter(journal => journal && journal.trim() !== '')
              .join(';') || '无' }}
        </template>
      </el-table-column>

      <!-- 奖项列 -->
      <el-table-column
        label="奖项"
        min-width="80"
      >
        <template #default="scope">
          {{ [scope.row.award1_awardName, scope.row.award2_awardName, scope.row.award3_awardName]
              .filter(award => award && award.trim() !== '')
              .join(';') || '无' }}
        </template>
      </el-table-column>

      <!-- 文件下载列 -->
      <el-table-column
        label="证明文件"
        min-width="80"
      >
        <template #default="scope">
          <el-link
            v-if="scope.row.file_path"
            type="primary"
            :href="getFileDownloadUrl(scope.row.file_path)"
            target="_blank"
          >
            {{ scope.row.file_name }}
          </el-link>
          <span v-else>无文件</span>
        </template>
      </el-table-column>
    </el-table>

    <!-- 错误提示 -->
    <div v-if="store.error" class="error-message">
      {{ store.error }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref, computed } from 'vue';
import { useResultStore } from '@/stores/resultStore';
import { getFileDownloadUrl } from '@/apis/files';
import { useFieldStore } from '@/stores/fieldStore';
import * as XLSX from 'xlsx';

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

// 组件挂载时获取数据
onMounted(() => {
  store.fetchFilteredStudents();
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
</script>

<style scoped>
.result-table {
  padding: 20px;
}

.error-message {
  color: #f56c6c;
  margin-top: 10px;
  text-align: center;
}
</style>