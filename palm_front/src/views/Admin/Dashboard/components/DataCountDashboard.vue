<template>
  <el-card class="dashboard-card" :body-style="{ padding: '20px' }">
    <div class="dashboard-title">数据条数</div>
    <div class="data-count">{{ totalCount }} 条</div>
  </el-card>
</template>

<script>
export default {
  name: 'DataCountDashboard',
  data() {
    return {
      totalCount: 2000, // 模拟数据
    };
  },
};
</script>

<style scoped>
.dashboard-card {
  width: 100%;
  height: 100%;
  text-align: center;
}
.dashboard-title {
  margin-bottom: 10px;
  font-weight: bold;
}
.data-count {
  font-size: 20px;
  font-weight: bold;
}
</style>