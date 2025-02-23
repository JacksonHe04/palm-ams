<template>
  <div>
    <el-form :model="store.admissionPeriod" label-width="120px">
      <el-form-item label="开始日期">
        <div class="flex items-center gap-4">
          <el-date-picker
            v-model="store.admissionPeriod.startDate"
            type="date"
            value-format="YYYY-MM-DD"
            placeholder="选择开始日期"
          ></el-date-picker>
        </div>
      </el-form-item>
      <el-form-item label="结束日期">
        <div class="flex items-center gap-4">
          <el-date-picker
            v-model="store.admissionPeriod.endDate"
            type="date"
            value-format="YYYY-MM-DD"
            placeholder="选择结束日期"
          ></el-date-picker>
        </div>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleSaveAdmissionPeriod">提交</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup lang="ts">
import { watch } from 'vue';
import { useSettingStore } from '@/stores/settingStore';
import { ElMessage } from 'element-plus';

const store = useSettingStore();

const handleSaveAdmissionPeriod = async () => {
  try {
    await store.saveAdmissionPeriod();
    ElMessage.success('招生时间提交成功');
  } catch (error) {
    ElMessage.error('招生时间提交失败');
  }
};

watch([() => store.admissionPeriod.startDate, () => store.admissionPeriod.endDate], () => {
  if (!store.isInitializing) {
    ElMessage.warning('您已修改招生时间，请记得提交更改');
  }
});
</script>