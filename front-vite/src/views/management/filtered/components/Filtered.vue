<script setup lang="ts">
import { ref } from 'vue'
import {
  ElCard,
  ElTable,
  ElTableColumn,
  ElButton,
  ElTag,
} from 'element-plus'

// 模拟的表格数据
const tableData = ref([
  {
    id: 1,
    name: '张三',
    gender: '男',
    age: 18,
    grade: 12,
    score: 89,
    class: '高三(1)班',
    status: '已录取',
  },
  {
    id: 2,
    name: '李四',
    gender: '女',
    age: 17,
    grade: 12,
    score: 92,
    class: '高三(2)班',
    status: '待审核',
  },
  // 这里只是示例数据，实际使用时需要通过 API 获取真实数据
])

// 根据状态返回不同的标签类型
const getStatusType = (status: string) => {
  const statusMap: Record<string, 'success' | 'warning' | 'info'> = {
    '已录取': 'success',
    '待审核': 'warning',
    '未通过': 'info',
  }
  return statusMap[status] || 'info'
}
</script>

<template>
  <div class="p-6">
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-2xl font-bold">筛选结果</h2>
      <div class="flex gap-2">
        <el-button type="primary" @click="$router.push('/admin/filter')">
          返回筛选方案管理
        </el-button>
      </div>
    </div>

    <el-card class="mb-4">
      <template #header>
        <div class="flex justify-between items-center">
          <span class="font-semibold">学生信息表格</span>
          <div class="text-gray-500 text-sm">
            共 {{ tableData.length }} 条记录
          </div>
        </div>
      </template>

      <el-table
        :data="tableData"
        border
        stripe
        style="width: 100%"
      >
        <el-table-column
          prop="id"
          label="ID"
          width="80"
          align="center"
        />
        <el-table-column
          prop="name"
          label="姓名"
          width="120"
        />
        <el-table-column
          prop="gender"
          label="性别"
          width="80"
          align="center"
        />
        <el-table-column
          prop="age"
          label="年龄"
          width="80"
          align="center"
        />
        <el-table-column
          prop="grade"
          label="年级"
          width="100"
          align="center"
        />
        <el-table-column
          prop="class"
          label="班级"
          width="120"
        />
        <el-table-column
          prop="score"
          label="分数"
          width="100"
          align="center"
        />
        <el-table-column
          prop="status"
          label="状态"
          align="center"
        >
          <template #default="{ row }">
            <el-tag :type="getStatusType(row.status)">
              {{ row.status }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column
          label="操作"
          width="200"
          align="center"
        >
          <template #default="{ row }">
            <el-button
              size="small"
              type="primary"
              @click="() => {}"
            >
              查看详情
            </el-button>
            <el-button
              size="small"
              type="success"
              @click="() => {}"
            >
              编辑
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<style lang="scss" scoped>
.el-card {
  @apply bg-white rounded-lg shadow-sm;
}

:deep(.el-table) {
  @apply rounded-lg;
  
  th {
    @apply bg-gray-50;
  }
}
</style>