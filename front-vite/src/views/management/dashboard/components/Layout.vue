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
  </el-row>
</template>

<script>
import SchoolLevelDashboard from "@/views/management/dashboard/components/SchoolLevelDashboard.vue";
import MajorDistributionDashboard from "@/views/management/dashboard/components/MajorDistributionDashboard.vue";

import SchoolDistributionDashboard from "@/views/management/dashboard/components/SchoolDistributionDashboard.vue";
import EnrollmentTypeDashboard from "@/views/management/dashboard/components/EnrollmentTypeDashboard.vue";

export default {
  name: 'DashboardLayout',
  components: {
    SchoolLevelDashboard,
    MajorDistributionDashboard,
    SchoolDistributionDashboard,
    EnrollmentTypeDashboard,
  },
};
</script>