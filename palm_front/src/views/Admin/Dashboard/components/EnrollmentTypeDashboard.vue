<template>
  <el-card class="dashboard-card" :body-style="{ padding: '20px' }">
    <div class="dashboard-title">报名类型统计</div>
    <el-progress :percentage="masterPercentage" type="circle" status="success" width="120" />
    <el-progress :percentage="doctorPercentage" type="circle" status="warning" width="120" />
    <el-progress :percentage="directDoctorPercentage" type="circle" status="exception" width="120" />
  </el-card>
</template>

<script>
export default {
  name: 'EnrollmentTypeDashboard',
  data() {
    return {
      masterPercentage: 50, // 模拟数据
      doctorPercentage: 30, // 模拟数据
      directDoctorPercentage: 20, // 模拟数据
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
</style>