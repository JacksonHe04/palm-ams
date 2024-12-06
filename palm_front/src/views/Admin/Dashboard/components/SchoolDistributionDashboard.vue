<template>
  <el-card class="dashboard-card" :body-style="{ padding: '20px' }">
    <div class="dashboard-title">院校分布</div>
    <el-chart :data="barChartData" type="bar" />
  </el-card>
</template>

<script>
export default {
  name: 'SchoolDistributionDashboard',
  data() {
    return {
      barChartData: [
        { name: '清华大学', value: 50 },
        { name: '北京大学', value: 30 },
        { name: '复旦大学', value: 20 },
      ], // 模拟数据
    };
  },
};
</script>

<style scoped>
.dashboard-card {
  width: 100%;
  height: 100%;
}
.dashboard-title {
  margin-bottom: 10px;
  font-weight: bold;
}
</style>