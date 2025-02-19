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

      <!-- 基本信息列 -->
      <el-table-column prop="name" label="姓名" min-width="100" />
      <el-table-column prop="applicationType" label="报名类型" min-width="120" />
      <el-table-column prop="university" label="本科学校" min-width="150" />
      <el-table-column prop="universityLevel" label="本科等级" min-width="100" />
      <el-table-column prop="major" label="本科专业" min-width="150" />
      <el-table-column prop="percentage" label="百分比" min-width="100" />
      <el-table-column prop="masterUniversity" label="硕士学校" min-width="150" />
      <el-table-column prop="masterUniversityLevel" label="硕士等级" min-width="100" />
      <el-table-column prop="masterMajor" label="硕士专业" min-width="150" />
      <el-table-column prop="tutor" label="导师" min-width="100" />
      <el-table-column prop="status" label="状态" min-width="100" />
    </el-table>

    <!-- 错误提示 -->
    <div v-if="store.error" class="error-message">
      {{ store.error }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useResultStore } from '@/stores/resultStore';

// 初始化 store
const store = useResultStore();

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