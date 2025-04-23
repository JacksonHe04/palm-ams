<script setup>
import { onMounted } from 'vue';
import { useResultStore } from '@/stores/resultStore';

const store = useResultStore();

onMounted(async () => {
  await store.fetchFailedStudents();
  console.log('未通过筛选的学生:', store.failedStudents);
});
</script>

<template>
  <div class="p-6">
    <el-card>
      <template #header>
        <div class="flex justify-between items-center">
          <div class="flex items-start flex-col">
            <span class="text-xl font-bold">未通过筛选学生</span>
            <div class="text-gray-500 text-sm mt-1">
              查看未通过筛选的学生的申请信息
            </div>
          </div>
        </div>
      </template>

      <el-table
        v-loading="store.loading"
        :data="store.failedStudents"
        style="width: 100%"
        border
        :table-layout="'auto'"
      >
        <el-table-column type="index" label="#" width="50" />
        <el-table-column prop="name" label="姓名" />
        <el-table-column prop="university" label="本科院校" />
        <el-table-column prop="masterUniversity" label="硕士院校" />
        <el-table-column prop="percentage" label="排名百分比" />
        <el-table-column prop="applicationType" label="申请类型" />
      </el-table>

      <div v-if="store.error" class="error-message mt-4 text-red-500">
        {{ store.error }}
      </div>
    </el-card>
  </div>
</template>

<style scoped>
.error-message {
  color: #f56c6c;
  margin-top: 10px;
}
</style>