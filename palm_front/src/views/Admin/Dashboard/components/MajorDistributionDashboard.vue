<template>
  <el-card class="dashboard-card" :body-style="{ padding: '20px' }">
    <div class="dashboard-title">专业分布</div>
    <el-chart :data="barChartData" type="bar" />
  </el-card>
</template>

<script>
export default {
  name: 'MajorDistributionDashboard',
  data() {
    return {
      barChartData: [
        { name: '计算机', value: 50 },
        { name: '电子工程', value: 30 },
        { name: '机械工程', value: 20 },
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