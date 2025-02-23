<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <el-tabs type="border-card" class="bg-white rounded-lg shadow-lg" v-loading="store.isLoading">
      <el-tab-pane label="院校等级调整">
        <UniversityLevel />
      </el-tab-pane>

      <el-tab-pane label="专业分类调整">
        <MajorCategory />
      </el-tab-pane>

      <el-tab-pane label="人员身份调整">
        <PersonnelManagement />
      </el-tab-pane>

      <el-tab-pane label="招生年份和时间调整">
        <AdmissionPeriod />
      </el-tab-pane>

      <el-tab-pane label="奖项配置">
        <AwardSetting />
      </el-tab-pane>

      <el-tab-pane label="年份配置">
        <YearSetting />
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useSettingStore } from '@/stores/settingStore';
import UniversityLevel from './components/UniversityLevel.vue';
import MajorCategory from './components/MajorCategory.vue';
import PersonnelManagement from './components/PersonnelManagement.vue';
import AdmissionPeriod from './components/AdmissionPeriod.vue';
import AwardSetting from './components/AwardSetting.vue';
import YearSetting from './components/YearSetting.vue';

const store = useSettingStore();

// 初始化数据
onMounted(async () => {
  await store.initializeData();
});
</script>

<style scoped>
.el-tabs {
  @apply shadow-md rounded-lg;
}

.el-tab-pane {
  @apply p-6;
}

.el-button {
  @apply transition-colors duration-200;
}

.el-button:hover {
  @apply opacity-80;
}

.el-table {
  @apply rounded-lg overflow-hidden;
}
</style>