<template>
  <el-card class="dashboard-card" :body-style="{ padding: '20px' }">
    <div class="dashboard-title">专业分布</div>
    <div ref="chart" style="width: 100%; height: 300px;"></div>
  </el-card>
</template>

<script>
import * as echarts from 'echarts';

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
  mounted() {
    this.initChart();
  },
  methods: {
    initChart() {
      const chartDom = this.$refs.chart;
      const myChart = echarts.init(chartDom);
      const option = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        xAxis: {
          type: 'category',
          data: this.barChartData.map(item => item.name)
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: '专业分布',
            type: 'bar',
            data: this.barChartData.map(item => item.value)
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
}
.dashboard-title {
  margin-bottom: 10px;
  font-weight: bold;
}
</style>
