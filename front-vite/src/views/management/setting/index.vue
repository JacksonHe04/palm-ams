<template>
  <div class="p-6">
    <el-card>
      <template #header>
        <div class="flex justify-between items-center">
          <div class="flex items-start flex-col">
            <span class="text-xl font-bold">系统设置</span>
            <div class="text-gray-500 text-sm mt-1">
              管理系统的基础配置信息
            </div>
          </div>
        </div>
      </template>

      <el-tabs v-model="activeTab" v-loading="store.isLoading">
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
      </el-tabs>

      <!-- 错误提示 -->
      <div v-if="store.error" class="error-message">
        {{ store.error }}
      </div>
    </el-card>
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
  admission: defineAsyncComponent(() => import('./components/DateSetting.vue')),
  award: defineAsyncComponent(() => import('./components/AwardSetting.vue')),
  year: defineAsyncComponent(() => import('./components/YearSetting.vue'))
});

const currentComponent = computed(() => components.value[activeTab.value]);
</script>

<style lang="scss" scoped>
.el-table {
  --el-table-border-color: #dcdfe6;
  --el-table-header-bg-color: #f5f7fa;

  :deep(th) {
    font-weight: 600;
    color: #606266;
  }
}

.error-message {
  color: #f56c6c;
  margin-top: 10px;
  text-align: center;
}

.el-tabs {
  :deep(.el-tabs__header) {
    margin-bottom: 16px;
  }
}
</style>