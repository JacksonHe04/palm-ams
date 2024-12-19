<template>
  <div class="analysis-block">
    <el-card class="box-card">
      <template #header>
        <span>学生数据分析</span>
      </template>
      <div class="charts-container">
        <div ref="studentCountChart" class="chart"></div>
        <div ref="applicationTypeChart" class="chart"></div>
        <div ref="universityChart" class="chart"></div>
        <div ref="interviewScoreChart" class="chart"></div>
        <!-- 可以继续添加其他图表 -->
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useStudentsStore } from '@/stores/studentsStore';
import * as echarts from 'echarts';

const studentsStore = useStudentsStore();
const studentCountChart = ref(null);
const applicationTypeChart = ref(null);
const universityChart = ref(null);
const interviewScoreChart = ref(null);

onMounted(async () => {
  await studentsStore.fetchStudents();
  initStudentCountChart();
  initApplicationTypeChart();
  initUniversityChart();
  initInterviewScoreChart();
});

function initStudentCountChart() {
  const chart = echarts.init(studentCountChart.value);
  const option = {
    title: {
      text: '学生总数',
      subtext: studentsStore.students.length,
      left: 'center'
    },
    tooltip: {
      formatter: '{a} <br/>{b} : {c}'
    },
    series: [
      {
        name: '学生总数',
        type: 'gauge',
        detail: {
          formatter: '{value}'
        },
        data: [
          {
            value: studentsStore.students.length,
            name: '学生总数'
          }
        ]
      }
    ]
  };
  chart.setOption(option);
}

function initApplicationTypeChart() {
  const chart = echarts.init(applicationTypeChart.value);
  const applicationTypes = studentsStore.students.reduce((acc, student) => {
    acc[student.applicationType] = (acc[student.applicationType] || 0) + 1;
    return acc;
  }, {});

  const option = {
    title: {
      text: '报名类型分布',
    },
    tooltip: {
      trigger: 'item',
    },
    legend: {
      top: '5%',
      left: 'center',
    },
    series: [
      {
        name: '报名类型',
        type: 'pie',
        radius: '50%',
        data: Object.entries(applicationTypes).map(([name, value]) => ({ name, value })),
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)',
          },
        },
      },
    ],
  };
  chart.setOption(option);
}

function initUniversityChart() {
  const chart = echarts.init(universityChart.value);
  const universities = studentsStore.students.reduce((acc, student) => {
    acc[student.university] = (acc[student.university] || 0) + 1;
    return acc;
  }, {});

  const option = {
    title: {
      text: '本科学校分布',
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow',
      },
    },
    xAxis: {
      type: 'category',
      data: Object.keys(universities),
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        name: '数量',
        data: Object.values(universities),
        type: 'bar',
      },
    ],
  };
  chart.setOption(option);
}

function initInterviewScoreChart() {
  const chart = echarts.init(interviewScoreChart.value);
  // 编造一组面试分数数据
  const interviewScores = [85, 90, 90, 78, 78, 92, 88, 76, 95, 89, 89, 84, 84, 91, 87, 82, 93, 86, 94];
  const scoreCounts = interviewScores.reduce((acc, score) => {
    acc[score] = (acc[score] || 0) + 1;
    return acc;
  }, {});

  const option = {
    title: {
      text: '面试分数分布',
    },
    tooltip: {},
    xAxis: {
      type: 'category',
      data: Object.keys(scoreCounts).map(Number).sort((a, b) => a - b),
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        name: '数量',
        data: Object.values(scoreCounts),
        type: 'bar',
      },
    ],
  };
  chart.setOption(option);
}
</script>

<style scoped>
.analysis-block {
  padding: 20px;
}

.charts-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.chart {
  width: 45%;
  height: 400px;
}
</style>
