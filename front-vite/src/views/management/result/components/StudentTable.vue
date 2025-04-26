<template>
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
      label="论文"
      min-width="80"
    >
      <template #default="scope">
        {{ [scope.row.paper1_journalConference, scope.row.paper2_journalConference, scope.row.paper3_journalConference]
            .filter(journal => journal && journal.trim() !== '')
            .join(';') || '无' }}
      </template>
    </el-table-column>

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
</template>

<script setup lang="ts">
import { getFileDownloadUrl } from '@/apis/files';

const props = defineProps<{
  data: any[];
  loading: boolean;
  columnConfig: Record<string, { label: string; width: string }>;
}>();

const emit = defineEmits<{
  (e: 'selectionChange', selection: any[]): void;
}>();

/**
 * 处理表格多选变化
 * @param selection 当前选中的行数据数组
 */
const handleSelectionChange = (selection: any[]) => {
  emit('selectionChange', selection);
};
</script>