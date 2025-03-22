<template>
  <div class="new-apply-container">
    <form @submit.prevent="handleSubmit" class="apply-form">
      <div v-for="field in applyFields" :key="field.id" class="form-item">
        <label :for="field.variableName">{{ field.name }}</label>
        <div class="field-description">{{ field.description }}</div>
        
        <input
          v-if="(field.type === 'text' || field.type === 'number' || field.type === 'email') && field.variableName !== 'percentage'"
          :type="field.type"
          :id="field.variableName"
          v-model="formData[field.variableName]"
          :name="field.variableName"
          class="form-input"
          :required="isFieldRequired(field.variableName)"
          @input="field.variableName === 'rank' || field.variableName === 'majorCount' ? calculatePercentage() : null"
        />

        <!-- 百分比 -->
        <input
          v-else-if="field.variableName === 'percentage'"
          type="text"
          :id="field.variableName"
          :value="formData[field.variableName]"
          :name="field.variableName"
          class="form-input"
          disabled
        />
        
        <!-- 文本域 -->
        <textarea
          v-else-if="field.type === 'textarea'"
          :id="field.variableName"
          v-model="formData[field.variableName]"
          :name="field.variableName"
          class="form-textarea"
          :required="isFieldRequired(field.variableName)"
        ></textarea>
        
        <!-- 自动搜索下拉框 -->
        <AutoCompleteInput
          v-if="field.type === 'select' && ['本科学校', '硕士学校', '本科专业', '硕士专业'].includes(field.name)"
          v-model="formData[field.variableName]"
          :options="getSelectOptions(field.name)"
          :placeholder="'请输入' + field.name"
        />
        
        <!-- 普通单选下拉框 -->
        <select
          v-else-if="field.type === 'select'"
          :id="field.variableName"
          v-model="formData[field.variableName]"
          :name="field.variableName"
          class="form-select"
          :required="isFieldRequired(field.variableName)"
        >
          <option value="">请选择</option>
          <option
            v-for="option in getSelectOptions(field.name)"
            :key="option.value"
            :value="option.value"
          >
            {{ option.label }}
          </option>
        </select>

        <!-- 开关 -->
        <el-switch
          v-else-if="field.type === 'boolean'"
          :id="field.variableName"
          v-model="formData[field.variableName]"
          :name="field.variableName"
          class="form-switch"
          :required="isFieldRequired(field.variableName)"
        />
        
        <!-- 奖项贡献字段 -->
        <div v-else-if="['award1_contribution', 'award2_contribution', 'award3_contribution'].includes(field.variableName)" class="flex gap-4 items-center">
          <div class="flex-1">
            <input
              type="number"
              :id="`${field.variableName}_rank`"
              v-model="contributionData[field.variableName].rank"
              class="form-input"
              placeholder="贡献排名"
              min="1"
              @input="updateContribution(field.variableName)"
            />
          </div>
          <span class="text-gray-500">/</span>
          <div class="flex-1">
            <input
              type="number"
              :id="`${field.variableName}_total`"
              v-model="contributionData[field.variableName].total"
              class="form-input"
              placeholder="团队人数"
              min="1"
              @input="updateContribution(field.variableName)"
            />
          </div>
        </div>
        
        <!-- 其他类型 -->
        <input
          v-else-if="(field.type === 'string' || field.type === 'date') && field.variableName !== 'percentage'"
          :type="field.type"
          :id="field.variableName"
          v-model="formData[field.variableName]"
          :name="field.variableName"
          class="form-input"
          :required="isFieldRequired(field.variableName)"
        />
      </div>
      
      <!-- 上传简历 -->
      <UploadResume />
      
      <!-- 证明文件上传 -->
      <UploadFile :applicant-id="formData.id" />
      
      <button type="submit" class="submit-button">提交申请</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { onMounted, computed } from 'vue'
import router from '@/router'
import { ElSwitch, ElMessage } from 'element-plus'
import { v4 as uuidv4 } from 'uuid'

import { useFieldStore } from '@/stores/fieldStore'
import { useSettingStore } from '@/stores/settingStore'
import { useFormValidation } from './composables/useFormValidation'
import { usePercentageCalculation } from './composables/usePercentageCalculation'
import { useApplyStore } from '@/stores/applyStore'

import UploadFile from './components/UploadFile.vue'
import AutoCompleteInput from './components/AutoCompleteInput.vue'
import UploadResume from './components/UploadResume.vue'

const fieldStore = useFieldStore()
const settingStore = useSettingStore()

import { ccfLevel, awardLevel, awardRanking, applicationType, gender } from './composables/formConfig'
// 选项配置对象
const selectOptions = computed(() => ({
  '报名类型': applicationType,
  '性别': gender,
  '论文一CCF等级': ccfLevel,
  '论文二CCF等级': ccfLevel,
  '论文三CCF等级': ccfLevel,
  '奖项一等级': awardLevel,
  '奖项二等级': awardLevel,
  '奖项三等级': awardLevel,
  '奖项一获奖等级': awardRanking,
  '奖项二获奖等级': awardRanking,
  '奖项三获奖等级': awardRanking,
  '本科学校': settingStore.universities.map(uni => ({
    value: uni.name,
    label: uni.name
  })),
  '硕士学校': settingStore.universities.map(uni => ({
    value: uni.name,
    label: uni.name
  })),
  '第一志愿': settingStore.personnel.map(person => ({
    value: person.name,
    label: `${person.name} (${person.research_direction})`
  })),
  '第二志愿': settingStore.personnel.map(person => ({
    value: person.name,
    label: `${person.name} (${person.research_direction})`
  })),
  '第三志愿': settingStore.personnel.map(person => ({
    value: person.name,
    label: `${person.name} (${person.research_direction})`
  })),
  '本科专业': settingStore.majors.map(major => ({
    value: major.name,
    label: major.name
  })),
  '硕士专业': settingStore.majors.map(major => ({
    value: major.name,
    label: major.name
  }))
}))

// 获取下拉选项
const getSelectOptions = (fieldName: string) => {
  return selectOptions.value[fieldName] || []
}

// 获取需要在申请表单中显示的字段
const applyFields = computed(() => {
  return fieldStore.fields.filter(field => field.showInApply)
})

// 导入表单验证组合式函数
const { isFieldRequired, validateForm } = useFormValidation()

// 提交表单
const handleSubmit = async () => {
  try {
    validateForm(formData.value, applyFields.value)
    await applyStore.submitForm()
    ElMessage.success('申请提交成功')
    router.push('/wait')
    
  } catch (error) {
    ElMessage.error(error.message || applyStore.submitError || '提交失败')
  }
}

const applyStore = useApplyStore()
const formData = computed(() => applyStore.formData)

// 导入百分比计算组合式函数
const { calculatePercentage, contributionData, updateContribution } = usePercentageCalculation(formData)

const initFormData = () => {
  const initialData = {
    id: uuidv4()
  }
  // 先初始化贡献度数据
  contributionData.value = {
    award1_contribution: { rank: '', total: '' },
    award2_contribution: { rank: '', total: '' },
    award3_contribution: { rank: '', total: '' }
  }
  
  applyFields.value.forEach(field => {
    if (['award1_contribution', 'award2_contribution', 'award3_contribution'].includes(field.variableName)) {
      initialData[field.variableName] = ''
    } else if (field.variableName === 'isAdjustable') {
      initialData[field.variableName] = true
    } else {
      initialData[field.variableName] = field.type === 'boolean' ? false : '';
    }
  })
  applyStore.setFormData(initialData)
}

onMounted(async () => {
  await Promise.all([
    fieldStore.fetchFields(),
    settingStore.fetchUniversities(),
    settingStore.fetchMajors(),
    settingStore.fetchPersonnel()
  ])
  initFormData()
})
</script>

<style lang="scss" scoped>
@use '@/styles/views/front-desk/new_apply/index.scss';
</style>