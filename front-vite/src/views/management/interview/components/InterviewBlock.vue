<template>
  <div class="interview-block p-6">
    <el-card class="mb-6">
      <template #header>
        <div class="card-header text-left">
          <span class="text-xl font-bold">面试评分</span>
          <div class="text-gray-500 text-sm mt-1">
            导入面试评分表格并进行归一化处理
          </div>
        </div>
      </template>

      <!-- 添加文件输入元素，并隐藏它 -->
      <input type="file" ref="fileInput" @change="handleFileUpload" accept=".xlsx,.xls" style="display: none;" />

      <!-- 将按钮的点击事件改为触发文件输入元素的点击 -->
      <el-button type="primary" @click="triggerFileInput">导入表格</el-button>
      <el-button type="success" @click="normalizeScores">归一化</el-button>

      <el-table
        :data="tableData"
        style="width: 100%; margin-top: 20px;"
        :default-sort="{ prop: 'normalizedScore', order: 'descending' }"
        table-layout="fixed"
        border
      >
        <el-table-column type="index" label="序号" min-width="60"></el-table-column>
        <el-table-column prop="student" label="学生" min-width="100"></el-table-column>
        <el-table-column prop="scoreTeacher1" label="老师一打分" min-width="100"></el-table-column>
        <el-table-column prop="scoreTeacher2" label="老师二打分" min-width="100"></el-table-column>
        <el-table-column prop="scoreTeacher3" label="老师三打分" min-width="100"></el-table-column>
        <el-table-column prop="normalizedScore" label="归一化打分" min-width="100" sortable></el-table-column>
        <el-table-column prop="resumeScore" label="简历分数" min-width="100"></el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import * as XLSX from 'xlsx';
import { ElMessage } from 'element-plus';
import { uploadInterviewScores, getNormalizedScores } from '@/apis/interview';

const tableData = ref([]);
const fileInput = ref(null);

// 触发文件输入元素的点击事件
const triggerFileInput = () => {
  fileInput.value.click();
};

// 处理文件上传
const handleFileUpload = async (event) => {
  const file = event.target.files[0];
  if (file) {
    try {
      // 读取Excel文件
      const reader = new FileReader();
      reader.onload = async (e) => {
        const data = e.target.result;
        const workbook = XLSX.read(data, { type: 'array' });
        const firstSheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[firstSheetName];
        const jsonData = XLSX.utils.sheet_to_json(worksheet);

        // 格式化数据
        const formattedData = jsonData.map(row => ({
          student: row.student || row['学生'],
          scoreTeacher1: Number(row.scoreTeacher1 || row['老师一打分']),
          scoreTeacher2: Number(row.scoreTeacher2 || row['老师二打分']),
          scoreTeacher3: Number(row.scoreTeacher3 || row['老师三打分']),
          resumeScore: Number(row.resumeScore || row['简历分数'] || 0)
        }));

        // 上传数据到服务器
        await uploadInterviewScores(file);
        tableData.value = formattedData;
        ElMessage.success('表格导入成功');
      };
      reader.readAsArrayBuffer(file);
    } catch (error) {
      console.error('文件处理错误:', error);
      ElMessage.error('表格导入失败');
    }
  }
};

// 归一化处理
const normalizeScores = async () => {
  try {
    const response = await getNormalizedScores();
    console.log('归一化数据:', response);
    
    // 确保我们使用正确的数据源
    const normalizedData = Array.isArray(response.data) ? response.data : response;
    
    // 确保数据格式正确
    const formattedData = normalizedData.map(row => ({
      student: row.student,
      scoreTeacher1: Number(row.scoreTeacher1),
      scoreTeacher2: Number(row.scoreTeacher2),
      scoreTeacher3: Number(row.scoreTeacher3),
      normalizedScore: Number(row.normalizedScore),
      resumeScore: Number(row.resumeScore || 0)
    }));

    tableData.value = formattedData;
    ElMessage.success('归一化处理完成');
  } catch (error) {
    console.error('归一化处理错误:', error);
    ElMessage.error('归一化处理失败');
  }
};
</script>

<style scoped>
.interview-block {
  padding: 20px;
}

.interview-block .el-table {
  width: 100%;
  overflow-x: auto;
}

/* 将按钮的对齐方式改为靠左 */
.interview-block .el-button {
  margin-right: 10px;
}

.interview-block .el-button + .el-button {
  margin-left: 0;
}

.interview-block .el-button:first-child {
  margin-left: 0;
}
</style>
