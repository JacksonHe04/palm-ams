<template>
  <div class="date-setting">
    <!-- 当前招生年份选择 -->
    <div class="mb-8">
      <div class="flex items-center">
        <span class="mr-2">当前招生年份：</span>
        <el-select
          v-model="currentAdmissionYear"
          placeholder="请选择当前招生年份"
          class="w-48"
          @change="handleCurrentAdmissionYearChange"
        >
          <el-option
            v-for="year in yearOptions"
            :key="year"
            :label="year + '年'"
            :value="year"
          />
        </el-select>
      </div>
    </div>

    <DividerLine />
    <!-- 年份选择器 -->
    <div class="mt-8 mb-4">
      <div class="flex items-center">
        <span class="mr-2">招生日期设置：</span>
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
import { useSettingStore } from '@/stores/settingStore'
import DividerLine from '@/components/DividerLine.vue'
import { ElMessage } from 'element-plus'

const dateStore = useDateStore()
const settingStore = useSettingStore()

// 当前招生年份选择
const currentAdmissionYear = ref(new Date().getFullYear())
// console.log('当前年份1:', currentAdmissionYear.value)

// 获取当前招生年份
onMounted(async () => {
  try {
    // 获取当前招生年份
    await settingStore.fetchYear()
    // console.log('当前年份2:', settingStore.year.year)
    if (settingStore.year.year > 0) {
      currentAdmissionYear.value = settingStore.year.year
      selectedYear.value = currentAdmissionYear.value
      // console.log('当前招生年份:', currentAdmissionYear.value)
      // 确保初始化时加载数据
      await dateStore.fetchAdmissionDatesByYear(selectedYear.value)
    }
  } catch (error) {
    console.error('初始化数据失败:', error)
  }
})

// 处理当前招生年份变化
const handleCurrentAdmissionYearChange = async (year: number) => {
  try {
    await settingStore.saveYear(year)
    // 同步更新选中年份
    selectedYear.value = year
    // 加载新年份的数据
    await dateStore.fetchAdmissionDatesByYear(year)
    ElMessage.success('当前招生年份设置成功')
  } catch (error) {
    console.error('保存当前招生年份失败:', error)
    ElMessage.error('保存当前招生年份失败')
  }
}

// 年份选择
const selectedYear = ref(currentAdmissionYear.value)

// 生成年份选项（前后2年）
const yearOptions = computed(() => {
  const years = []
  const currentYear = new Date().getFullYear()
  for (let i = currentYear - 1; i <= currentYear + 2; i++) {
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
</script>

<style scoped lang="scss">
.date-setting {
  padding: 20px;
}
</style>