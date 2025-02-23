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
      <input type="file" ref="fileInput" @change="handleFileUpload" style="display: none;" />

      <!-- 将按钮的点击事件改为触发文件输入元素的点击 -->
      <el-button type="primary" @click="triggerFileInput">导入表格</el-button>
      <el-button type="success" @click="normalizeScores">归一化</el-button>

      <el-table
        :data="tableData"
        style="width: 100%; margin-top: 20px;"
        :default-sort="{ prop: 'normalizedScore', order: 'descending' }"
      >
        <el-table-column type="index" label="序号" width="50"></el-table-column>
        <el-table-column prop="student" label="学生" width="120"></el-table-column>
        <el-table-column prop="scoreTeacher1" label="老师一打分" width="120"></el-table-column>
        <el-table-column prop="scoreTeacher2" label="老师二打分" width="120"></el-table-column>
        <el-table-column prop="scoreTeacher3" label="老师三打分" width="120"></el-table-column>
        <el-table-column prop="normalizedScore" label="归一化打分" width="120" sortable></el-table-column>
        <el-table-column prop="resumeScore" label="简历分数" width="120"></el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const tableData = ref([]);
const fileInput = ref(null);

// 触发文件输入元素的点击事件
const triggerFileInput = () => {
  fileInput.value.click();
};

// 处理文件上传
const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    // 这里可以添加读取文件并解析数据的逻辑
    console.log('导入文件:', file);
    // 示例：读取Excel文件并解析数据
    // 可以使用第三方库如xlsx来处理Excel文件
  }
};

const normalizeScores = () => {
  // 这里可以添加归一化的逻辑
  // 例如：计算每个学生的归一化得分
  console.log('归一化');
};
</script>

<style scoped>
.interview-block {
  padding: 20px;
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
