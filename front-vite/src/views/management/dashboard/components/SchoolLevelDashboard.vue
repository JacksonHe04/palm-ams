<template>
  <el-card class="dashboard-card" :body-style="{ padding: '20px' }">
    <div class="dashboard-title">院校等级统计</div>
    <div id="school-level-chart" style="width: 100%; height: 300px;"></div>
  </el-card>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'SchoolLevelDashboard',
  data() {
    return {
      Apercentage: 60, // 模拟数据
      Bpercentage: 30, // 模拟数据
      Cpercentage: 10, // 模拟数据
    };
  },
  mounted() {
    this.initChart();
  },
  methods: {
  initChart() {
    const chartDom = document.getElementById('school-level-chart');
    const myChart = echarts.init(chartDom);
    const option = {
      tooltip: {
        trigger: 'item'
      },
      series: [
        {
          name: '院校等级',
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
            show: true // 显示引导线
          },
          data: [
            { value: this.Apercentage, name: 'A级' },
            { value: this.Bpercentage, name: 'B级' },
            { value: this.Cpercentage, name: 'C级' }
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
  text-align: center;
}
.dashboard-title {
  margin-bottom: 10px;
  font-weight: bold;
}
</style>
