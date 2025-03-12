<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <el-tabs type="border-card" class="bg-white rounded-lg shadow-lg" v-loading="store.isLoading" v-model="activeTab">
      <el-tab-pane label="院校等级调整" name="university">
        <component :is="currentComponent" v-if="activeTab === 'university'"/>
      </el-tab-pane>

      <el-tab-pane label="专业分类调整" name="major">
        <component :is="currentComponent" v-if="activeTab === 'major'"/>
      </el-tab-pane>

      <el-tab-pane label="奖项配置" name="award">
        <component :is="currentComponent" v-if="activeTab === 'award'"/>
      </el-tab-pane>

      <el-tab-pane label="导师信息调整" name="personnel">
        <component :is="currentComponent" v-if="activeTab === 'personnel'"/>
      </el-tab-pane>

      <el-tab-pane label="招生年份和时间调整" name="admission">
        <component :is="currentComponent" v-if="activeTab === 'admission'"/>
      </el-tab-pane>

      <el-tab-pane label="年份配置" name="year">
        <component :is="currentComponent" v-if="activeTab === 'year'"/>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
import { ref, shallowRef, computed, defineAsyncComponent } from 'vue';
import { useSettingStore } from '@/stores/settingStore';

const store = useSettingStore();
const activeTab = ref('university');

// 使用defineAsyncComponent来包装异步组件
const components = shallowRef({
  university: defineAsyncComponent(() => import('./components/UniversityLevel.vue')),
  major: defineAsyncComponent(() => import('./components/MajorCategory.vue')),
  personnel: defineAsyncComponent(() => import('./components/PersonnelManagement.vue')),
  admission: defineAsyncComponent(() => import('./components/AdmissionPeriod.vue')),
  award: defineAsyncComponent(() => import('./components/AwardSetting.vue')),
  year: defineAsyncComponent(() => import('./components/YearSetting.vue'))
});

const currentComponent = computed(() => components.value[activeTab.value]);
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