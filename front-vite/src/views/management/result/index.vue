<template>
  <div class="result-table">
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
      />
    </el-table>

    <!-- 错误提示 -->
    <div v-if="store.error" class="error-message">
      {{ store.error }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive } from 'vue';
import { useResultStore } from '@/stores/resultStore';

// 初始化 store
const store = useResultStore();

// 定义列配置
const columnConfig = reactive({
  name: { label: '姓名', width: '100' },
  applicationType: { label: '报名类型', width: '120' },
  university: { label: '本科学校', width: '150' },
  universityLevel: { label: '本科等级', width: '100' },
  major: { label: '本科专业', width: '150' },
  percentage: { label: '百分比', width: '100' },
  masterUniversity: { label: '硕士学校', width: '150' },
  masterUniversityLevel: { label: '硕士等级', width: '100' },
  masterMajor: { label: '硕士专业', width: '150' },
  tutor: { label: '导师', width: '100' },
  status: { label: '状态', width: '100' }
});

// 组件挂载时获取数据
onMounted(() => {
  store.fetchFilteredStudents();
});
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