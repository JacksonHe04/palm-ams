<template>
  <div class="date-setting">
    <!-- 年份选择器 -->
    <div class="mb-4">
      <el-select
        v-model="selectedYear"
        placeholder="请选择年份"
        class="w-48"
        @change="handleYearChange"
      >
        <el-option
          v-for="year in yearOptions"
          :key="year"
          :label="year + '年'"
          :value="year"
        />
      </el-select>
    </div>

    <!-- 招生时间表格 -->
    <el-table :data="dateStore.admissionDates" border v-loading="dateStore.isLoading">
      <el-table-column
        prop="type"
        label="招生类型"
        width="180"
      />
      <el-table-column label="开始时间">
        <template #default="{ row }">
          <el-date-picker
            v-model="row.start_time"
            type="datetime"
            placeholder="选择开始时间"
            format="YYYY-MM-DD HH:mm:ss"
            value-format="YYYY-MM-DD HH:mm:ss"
          />
        </template>
      </el-table-column>
      <el-table-column label="结束时间">
        <template #default="{ row }">
          <el-date-picker
            v-model="row.end_time"
            type="datetime"
            placeholder="选择结束时间"
            format="YYYY-MM-DD HH:mm:ss"
            value-format="YYYY-MM-DD HH:mm:ss"
          />
        </template>
      </el-table-column>
    </el-table>

    <!-- 保存按钮 -->
    <div class="mt-4 text-right">
      <el-button type="primary" @click="handleSave" :loading="dateStore.isLoading">
        保存设置
      </el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useDateStore } from '@/stores/dateStore'

const dateStore = useDateStore()

// 年份选择
const currentYear = new Date().getFullYear()
const selectedYear = ref(currentYear)

// 生成年份选项（前后5年）
const yearOptions = computed(() => {
  const years = []
  for (let i = currentYear - 2; i <= currentYear + 2; i++) {
    years.push(i)
  }
  return years
})

// 处理年份变化
const handleYearChange = async (year: number) => {
  await dateStore.fetchAdmissionDatesByYear(year)
}

// 处理保存
const handleSave = async () => {
  await dateStore.saveAdmissionDatesByYear(selectedYear.value)
}

// 组件挂载时初始化数据
onMounted(async () => {
  await dateStore.fetchAdmissionDatesByYear(currentYear)
})
</script>

<style scoped lang="scss">
.date-setting {
  padding: 20px;
}
</style>