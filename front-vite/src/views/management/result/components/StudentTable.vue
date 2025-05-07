<template>
  <div>
    <el-table
      v-loading="loading"
      :data="data"
      style="width: 100%"
      border
      :table-layout="'auto'"
      @selection-change="handleSelectionChange"
    >
      <el-table-column type="selection" width="55" />
      <el-table-column type="index" label="#" width="50" />
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

      <el-table-column
        label="证明文件"
        min-width="80"
      >
        <template #default="scope">
          <el-link
            v-if="scope.row.resume_file_path"
            type="primary"
            :href="getFileDownloadUrl(scope.row.resume_file_path)"
            target="_blank"
          >
            {{ scope.row.resume_file_name || '证明文件' }}
          </el-link>
          <span v-else>无证明文件</span>
        </template>
      </el-table-column>

      <el-table-column
        label="简历文件"
        min-width="80"
      >
        <template #default="scope">
          <el-link
            v-if="scope.row.proof_file_path"
            type="primary"
            :href="getFileDownloadUrl(scope.row.proof_file_path)"
            target="_blank"
          >
            {{ scope.row.proof_file_name || '简历文件' }}
          </el-link>
          <span v-else>无简历</span>
        </template>
      </el-table-column>
    </el-table>

    <!-- 错误提示 -->
    <div v-if="error" class="error-message">
      {{ error }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { getFileDownloadUrl } from '@/apis/files';

interface Student {
  id: number;
  resume_file_path?: string;
  resume_file_name?: string;
  proof_file_path?: string;
  proof_file_name?: string;
  [key: string]: any;
}

interface ColumnConfig {
  label: string;
  width: string;
}

const props = defineProps<{
  data: Student[];
  loading: boolean;
  error?: string;
  columnConfig: Record<string, ColumnConfig>;
}>();

const emit = defineEmits<{
  (e: 'selectionChange', selection: Student[]): void;
}>();

/**
 * 处理表格多选变化
 * @param selection 当前选中的行数据数组
 */
const handleSelectionChange = (selection: Student[]) => {
  emit('selectionChange', selection);
};
</script>

<style lang="scss" scoped>
.error-message {
  color: #f56c6c;
  margin-top: 10px;
  text-align: center;
}

.el-table {
  --el-table-border-color: #dcdfe6;
  --el-table-header-bg-color: #f5f7fa;

  :deep(th) {
    font-weight: 600;
    color: #606266;
  }
}
</style>