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
            <download-files
              :students="getStudentsByType(activeTab)"
              :selected-students="selectedStudents"
              :application-type="activeTab"
            />
            <export-excel
              :data="getStudentsByType(activeTab)"
              :column-config="columnConfig"
              :application-type="activeTab"
            />
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
            @selection-change="handleSelectionChange"
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
import { ElMessage } from 'element-plus';
import StudentTable from './components/StudentTable.vue';
import DownloadFiles from './components/DownloadFiles.vue';
import ExportExcel from './components/ExportExcel.vue';

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

// 选中的学生列表
const selectedStudents = ref<any[]>([]);

/**
 * 处理表格选择变化
 * @param selection 当前选中的行数据数组
 */
const handleSelectionChange = (selection: any[]) => {
  selectedStudents.value = selection;
};

// 监听标签页变化，清空选中状态
watch(activeTab, () => {
  selectedStudents.value = [];
});
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