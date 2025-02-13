<template>
  <el-card class="dashboard-card" :body-style="{ padding: '20px' }">
    <div class="dashboard-title">报名类型统计</div>
    <div id="enrollment-type-chart" style="width: 100%; height: 300px;"></div>
  </el-card>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'EnrollmentTypeDashboard',
  data() {
    return {
      masterPercentage: 50, // 模拟数据
      doctorPercentage: 30, // 模拟数据
      directDoctorPercentage: 20, // 模拟数据
    };
  },
  mounted() {
    this.initChart();
  },
  methods: {
    initChart() {
      const chartDom = document.getElementById('enrollment-type-chart');
      const myChart = echarts.init(chartDom);
      const option = {
        tooltip: {
          trigger: 'item'
        },
        series: [
          {
            name: '报名类型',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            label: {
              show: true, // 显示标签
              position: 'outside', // 标签位置设置为外部
              formatter: '{b}: {c}%' // 格式化标签显示内容
            },
            emphasis: {
              label: {
                show: false,
              }
            },
            labelLine: {
              show: true
            },
            data: [
              { value: this.masterPercentage, name: '硕士' },
              { value: this.doctorPercentage, name: '博士' },
              { value: this.directDoctorPercentage, name: '直博' }
            ]
          }
        ]
      };

      myChart.setOption(option);
    }
  }
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
