<template>
  <el-card class="dashboard-card" :body-style="{ padding: '20px' }">
    <div ref="chart" class="chart"></div>
  </el-card>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'DataCountDashboard',
  data() {
    return {
      chartInstance: null,
      totalCount: 2000, // 模拟数据
    };
  },
  mounted() {
    this.initChart();
  },
  methods: {
  initChart() {
    this.chartInstance = echarts.init(this.$refs.chart);
    const option = {
      series: [
        {
          type: 'gauge',
          axisLine: {
            show: false,
          },
          axisTick: {
            show: false,
          },
          splitLine: {
            show: false,
          },
          axisLabel: {
            show: false,
          },
          axisPointer: { // 添加这一行来隐藏指针
            show: false,
          },
          detail: {
            valueAnimation: true,
            fontSize: 40,
            fontWeight: 'bold',
            formatter: '{value} 条',
          },
          data: [
            {
              value: this.totalCount,
            },
          ],
        },
      ],
    };
    this.chartInstance.setOption(option);
  },
},

};
</script>

<style scoped>
.dashboard-card {
  width: 100%;
  height: 100%;
  text-align: center;
}
.chart {
  width: 100%;
  height: 200px;
}
</style>
