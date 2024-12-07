<template>
  <el-row class="dashboard-layout" gutter={20}>
    <el-col :span="12">
      <SchoolLevelDashboard />
    </el-col>
    <el-col :span="12">
      <EnrollmentTypeDashboard />

    </el-col>
    <el-col :span="12">
      <MajorDistributionDashboard />
    </el-col>
    <el-col :span="12">
      <SchoolDistributionDashboard />
    </el-col>
    <el-col :span="12">
      <DataCountDashboard />
    </el-col>
  </el-row>
</template>

<script>
import SchoolLevelDashboard from "@/views/Admin/Dashboard/components/SchoolLevelDashboard.vue";
import MajorDistributionDashboard from "@/views/Admin/Dashboard/components/MajorDistributionDashboard.vue";
import DataCountDashboard from "@/views/Admin/Dashboard/components/DataCountDashboard.vue";
import SchoolDistributionDashboard from "@/views/Admin/Dashboard/components/SchoolDistributionDashboard.vue";
import EnrollmentTypeDashboard from "@/views/Admin/Dashboard/components/EnrollmentTypeDashboard.vue";

export default {
  name: 'DashboardLayout',
  components: {
    SchoolLevelDashboard,
    MajorDistributionDashboard,
    DataCountDashboard,
    SchoolDistributionDashboard,
    EnrollmentTypeDashboard,
  },
};
</script>

<style scoped>
.dashboard-layout {
  margin-top: 20px;
  padding: 0 20px;
}
</style>