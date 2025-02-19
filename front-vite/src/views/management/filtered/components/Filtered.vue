<script setup lang="ts">
import { ref, onMounted } from 'vue'
import {
  ElCard,
  ElTable,
  ElTableColumn,
  ElButton,
  ElTag,
} from 'element-plus'
import { useFilterProcessorStore } from '@/stores/filterProcessorStore'

const filterStore = useFilterProcessorStore()
const tableData = ref([])

// 在组件挂载时获取筛选结果
onMounted(async () => {
  try {
    const filteredData = await filterStore.executeFilters()
    // 确保filteredData是数组类型
    if (!Array.isArray(filteredData)) {
      console.error('筛选数据格式错误：期望数组类型')
      return
    }
    // 处理数据中的null值和格式化，确保所有字段都有默认值
    tableData.value = filteredData.map(item => ({
      id: item.id || '',
      name: item.name || '',
      universityLevel: item.universityLevel || '',
      percentage: item.percentage || '0%',
      major: item.major || '未设置',
      isTopClass: item.isTopClass ?? false,
      isPaperCondition: item.isPaperCondition ?? false,
      isAwardCondition: item.isAwardCondition ?? false,
      isFilterCondition: item.isFilterCondition || 'false'
    }))
    console.log('处理后的表格数据:', tableData.value) // 添加日志以便调试
  } catch (error) {
    console.error('获取筛选数据失败:', error)
  }
})

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
          prop="universityLevel"
          label="本科等级"
          width="120"
          align="center"
        />
        <el-table-column
          prop="percentage"
          label="百分比"
          width="100"
          align="center"
        />
        <el-table-column
          prop="major"
          label="专业"
          width="150"
        />
        <el-table-column
          label="是否拔尖班"
          width="120"
          align="center"
        >
          <template #default="{ row }">
            <el-tag :type="row.isTopClass ? 'success' : 'info'">
              {{ row.isTopClass ? '是' : '否' }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column
          label="筛选状态"
          align="center"
        >
          <template #default="{ row }">
            <el-tag :type="row.isFilterCondition === 'true' ? 'success' : 'info'">
              {{ row.isFilterCondition === 'true' ? '通过筛选' : '未通过' }}
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