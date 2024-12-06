<template>
  <el-card class="dashboard-card" :body-style="{ padding: '20px' }">
    <div class="dashboard-title">院校等级统计</div>
    <el-progress :percentage="Apercentage" type="circle" status="success" width="120" />
    <el-progress :percentage="Bpercentage" type="circle" status="warning" width="120" />
    <el-progress :percentage="Cpercentage" type="circle" status="exception" width="120" />
  </el-card>
</template>

<script>
export default {
  name: 'SchoolLevelDashboard',
  data() {
    return {
      Apercentage: 60, // 模拟数据
      Bpercentage: 30, // 模拟数据
      Cpercentage: 10, // 模拟数据
    };
  },
};
</script>

<style scoped>
.dashboard-card {
  width: 100%;
  text-align: center;
}
.dashboard-title {
  margin-bottom: 10px;
  font-weight: bold;
}
</style>