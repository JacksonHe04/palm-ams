<template>
    <div class="percent-editor-container p-6">
      <el-card class="mb-6">
        <template #header>
          <div class="card-header text-left">
            <span class="text-xl font-bold">百分比设置</span>
            <div class="text-gray-500 text-sm mt-1">
              设置不同类别院校的录取百分比阈值
            </div>
          </div>
        </template>
  
        <el-form @submit.prevent="handleSubmit">
          <!-- A类院校设置 -->
          <div class="school-section mb-8">
            <h3 class="text-lg font-semibold mb-4 text-blue-600">A类院校</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <el-form-item label="普通">
                <el-input-number
                  v-model="percentStore.percentData.pOfA"
                  :min="0"
                  :max="100"
                  :precision="2"
                  :step="1"
                  class="w-full"
                  @change="handleDataChange"
                >
                  <template #suffix>%</template>
                </el-input-number>
              </el-form-item>
              <el-form-item label="拔尖班">
                <el-input-number
                  v-model="percentStore.percentData.pOfATop"
                  :min="0"
                  :max="100"
                  :precision="2"
                  :step="1"
                  class="w-full"
                  @change="handleDataChange"
                >
                  <template #suffix>%</template>
                </el-input-number>
              </el-form-item>
              <el-form-item label="人才">
                <el-input-number
                  v-model="percentStore.percentData.pOfATalent"
                  :min="0"
                  :max="100"
                  :precision="2"
                  :step="1"
                  class="w-full"
                  @change="handleDataChange"
                >
                  <template #suffix>%</template>
                </el-input-number>
              </el-form-item>
            </div>
          </div>
  
          <!-- B类院校设置 -->
          <div class="school-section mb-8">
            <h3 class="text-lg font-semibold mb-4 text-green-600">B类院校</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <el-form-item label="普通">
                <el-input-number
                  v-model="percentStore.percentData.pOfB"
                  :min="0"
                  :max="100"
                  :precision="2"
                  :step="1"
                  class="w-full"
                  @change="handleDataChange"
                >
                  <template #suffix>%</template>
                </el-input-number>
              </el-form-item>
              <el-form-item label="拔尖班">
                <el-input-number
                  v-model="percentStore.percentData.pOfBTop"
                  :min="0"
                  :max="100"
                  :precision="2"
                  :step="1"
                  class="w-full"
                  @change="handleDataChange"
                >
                  <template #suffix>%</template>
                </el-input-number>
              </el-form-item>
              <el-form-item label="人才">
                <el-input-number
                  v-model="percentStore.percentData.pOfBTalent"
                  :min="0"
                  :max="100"
                  :precision="2"
                  :step="1"
                  class="w-full"
                  @change="handleDataChange"
                >
                  <template #suffix>%</template>
                </el-input-number>
              </el-form-item>
            </div>
          </div>
  
          <!-- C类院校设置 -->
          <div class="school-section">
            <h3 class="text-lg font-semibold mb-4 text-yellow-600">C类院校</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <el-form-item label="普通">
                <el-input-number
                  v-model="percentStore.percentData.pOfC"
                  :min="0"
                  :max="100"
                  :precision="2"
                  :step="1"
                  class="w-full"
                  @change="handleDataChange"
                >
                  <template #suffix>%</template>
                </el-input-number>
              </el-form-item>
              <el-form-item label="拔尖班">
                <el-input-number
                  v-model="percentStore.percentData.pOfCTop"
                  :min="0"
                  :max="100"
                  :precision="2"
                  :step="1"
                  class="w-full"
                  @change="handleDataChange"
                >
                  <template #suffix>%</template>
                </el-input-number>
              </el-form-item>
              <el-form-item label="人才">
                <el-input-number
                  v-model="percentStore.percentData.pOfCTalent"
                  :min="0"
                  :max="100"
                  :precision="2"
                  :step="1"
                  class="w-full"
                  @change="handleDataChange"
                >
                  <template #suffix>%</template>
                </el-input-number>
              </el-form-item>
            </div>
          </div>
  
          <div class="flex justify-end mt-6">
            <el-button type="primary" :class="{ 'is-changed': isDataChanged }" @click="handleSubmit">保存设置</el-button>
          </div>
        </el-form>
      </el-card>
    </div>
  </template>
  
  <script setup lang="ts">
  import { onMounted, ref } from 'vue'
  import { usePercentStore } from '@/stores/percentStore'
  import { ElMessage } from 'element-plus'
  
  const percentStore = usePercentStore()
  const isDataChanged = ref(false)
  
  onMounted(() => {
    percentStore.fetchPercentData()
  })
  
  const handleDataChange = () => {
    isDataChanged.value = true
    ElMessage({
      message: '请记得点击保存按钮使配置生效',
      type: 'warning',
      duration: 3000
    })
  }
  
  const handleSubmit = async () => {
    await percentStore.updatePercentData(percentStore.percentData)
    isDataChanged.value = false
  }
  </script>
  
  <style lang="scss" scoped>
  .percent-editor-container {
    .el-card {
      @apply shadow-md;
    }
  
    .el-form-item {
      @apply mb-0;
  
      :deep(.el-form-item__label) {
        @apply text-gray-600 font-medium;
      }
    }
  
    .school-section {
      @apply p-4 rounded-lg bg-gray-50;
    }
  
    :deep(.el-input-number) {
      @apply w-full;
  
      .el-input__wrapper {
        @apply shadow-none;
      }
  
      .el-input__inner {
        @apply text-right;
      }
    }
  
    .is-changed {
      @apply animate-pulse;
    }
  }
  </style>