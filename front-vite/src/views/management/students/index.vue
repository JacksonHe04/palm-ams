<template>
  <div class="dev-notice ">
      <el-alert
        title="开发阶段提示"
        type="warning"
        description="当前页面的文件下载暂不可用，请前往“筛选结果”页面测试这一功能"
        :closable="false"
        show-icon
        center
      />
    </div>
  <div class="p-6">
    <el-card>
      <template #header>
        <div class="flex justify-between items-center">
          <div class="flex items-start flex-col">
            <span class="text-xl font-bold">学生列表</span>
            <div class="text-gray-500 text-sm mt-1">
              查看和导出所有学生的申请信息
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
            :loading="loading"
            :error="error"
            :column-config="columnConfig"
            @selection-change="handleSelectionChange"
          />
        </el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
  <el-dialog
    v-if="showDialog"
    title="提示"
    :visible.sync="showDialog"
    width="30%"
  >
    <span>未通过初筛的文件还没映射到总表格里（但是在系统里），这个今晚再解决。</span>
    <span slot="footer" class="dialog-footer">
      <el-button @click="showDialog = false">关闭</el-button>
    </span>
  </el-dialog>
</template>

<script setup lang="ts">
import { onMounted, ref, computed, watch } from 'vue';
import { useFieldStore } from '@/stores/fieldStore';
import { useFieldsSort } from '@/views/front-desk/apply/composables/useFieldsSort';
import StudentTable from '@/views/management/result/components/StudentTable.vue';
import DownloadFiles from '@/views/management/result/components/DownloadFiles.vue';
import ExportExcel from '@/views/management/result/components/ExportExcel.vue';
import { getStudents } from '@/apis/students';

interface Student {
  id: number;
  applicationType: string;
  [key: string]: any;
}

const showDialog = ref(true);

// 状态管理
const students = ref<Student[]>([]);
const loading = ref(false);
const error = ref('');

// 使用 fieldStore
const fieldStore = useFieldStore();

// 获取可展示的字段配置
const columnConfig = computed(() => {
  const showFields = fieldStore.fields.filter(field => field.showInTable);
  const { sortedFields } = useFieldsSort(showFields);
  
  return sortedFields.value.reduce((acc, field) => {
    acc[field.variableName] = {
      label: field.name,
      width: '150'
    };
    return acc;
  }, {} as Record<string, { label: string; width: string }>);
});

// 获取学生数据
const fetchStudents = async () => {
  loading.value = true;
  error.value = '';
  try {
    const data = await getStudents();
    students.value = data;
  } catch (err: any) {
    error.value = err.message || '获取学生数据失败';
  } finally {
    loading.value = false;
  }
};

// 在组件挂载时获取数据
onMounted(async () => {
  await fieldStore.fetchFields();
  await fetchStudents();
});

// 获取所有申请类型
const applicationTypes = computed(() => {
  const types = new Set(students.value.map(student => student.applicationType));
  return Array.from(types) as string[];
});

// 根据申请类型获取学生列表
const getStudentsByType = (type: string) => {
  return students.value.filter(student => student.applicationType === type);
};

// 当前激活的标签页
const activeTab = ref('');

// 监听 applicationTypes 的变化，自动设置第一个标签页
watch(applicationTypes, (types) => {
  if (types.length && !activeTab.value) {
    activeTab.value = types[0];
  }
}, { immediate: true });

// 选中的学生列表
const selectedStudents = ref<Student[]>([]);

const handleSelectionChange = (selection: Student[]) => {
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

