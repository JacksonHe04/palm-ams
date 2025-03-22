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
      
      <!-- 文件上传 -->
      <UploadFile :applicant-id="formData.id" />
      
      <button type="submit" class="submit-button">提交申请</button>
    </form>
  </div>
</template>

<script setup lang="ts">
// 在现有的 imports 后添加
import AutoCompleteInput from '@/components/AutoCompleteInput.vue'

import { ref, onMounted, computed } from 'vue'
import { useFieldStore } from '@/stores/fieldStore'
import { useSettingStore } from '@/stores/settingStore'
import { ElSwitch, ElMessage } from 'element-plus'
import { v4 as uuidv4 } from 'uuid'
import type { FieldItem } from '@/apis/field'
import { useApplyStore } from '@/stores/applyStore'
import UploadFile from '@/components/UploadFile.vue'

const fieldStore = useFieldStore()
const settingStore = useSettingStore()

const ccfLevel = [
    { value: 'A', label: 'A' },
    { value: 'B', label: 'B' },
    { value: 'C', label: 'C' },
    { value: '其他', label: '其他' }
  ]
const awardLevel = [
    { value: '国家级', label: '国家级' },
    { value: '省级', label: '省级' },
    { value: '校级', label: '校级' },
    { value: '其他', label: '其他' }
]
const awardRanking = [
    { value: '特等奖', label: '特等奖' },
    { value: '一等奖', label: '一等奖' },
    { value: '二等奖', label: '二等奖' },
    { value: '三等奖', label: '三等奖' },
    { value: '金奖', label: '金奖' },
    { value: '银奖', label: '银奖' },
    { value: '铜奖', label: '铜奖' },
]
// 选项配置对象
const selectOptions = computed(() => ({
  '报名类型': [
    { value: '硕士', label: '硕士' },
    { value: '博士', label: '博士' },
    { value: '直博', label: '直博' }
  ],
  '性别': [
    { value: '男', label: '男' },
    { value: '女', label: '女' }
  ],
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

const requiredFields = ref([
  'name',
  'applicationType'
])

// 获取需要在申请表单中显示的字段
const applyFields = computed(() => {
  return fieldStore.fields.filter(field => field.showInApply)
})

// 判断字段是否必填
const isFieldRequired = (fieldName: string) => {
  return requiredFields.value.includes(fieldName)
}

// 验证表单数据
const validateForm = () => {
  for (const fieldName of requiredFields.value) {
    const value = formData.value[fieldName]
    if (value === undefined || value === '' || (Array.isArray(value) && value.length === 0)) {
      const field = applyFields.value.find(f => f.variableName === fieldName)
      throw new Error(`${field?.name || fieldName}是必填项`)
    }
  }
  return true
}

// 提交表单
const handleSubmit = async () => {
  try {
    validateForm()
    await applyStore.submitForm()
    ElMessage.success('申请提交成功')
  } catch (error) {
    ElMessage.error(error.message || applyStore.submitError || '提交失败')
  }
}

const applyStore = useApplyStore()
const formData = computed(() => applyStore.formData)

// 初始化表单数据
const calculatePercentage = () => {
  const rank = Number(formData.value.rank)
  const majorCount = Number(formData.value.majorCount)
  if (!isNaN(rank) && !isNaN(majorCount) && majorCount !== 0) {
    const percentage = (rank / majorCount * 100).toFixed(2)
    applyStore.setFormData({
      ...formData.value,
      percentage: `${percentage}%`
    })
  } else {
    applyStore.setFormData({
      ...formData.value,
      percentage: ''
    })
  }
}

const initFormData = () => {
  const initialData = {
    id: uuidv4() // 在初始化时就生成一个临时ID
  }
  applyFields.value.forEach(field => {
    initialData[field.variableName] = field.type === 'boolean' ? false : ''
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

<style scoped>
.new-apply-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.apply-form {
  background: #ffffffa8;
  padding: 24px;
  border-radius: 18px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.form-item {
  margin-bottom: 24px;
}

label {
  display: block;
  font-weight: 600;
  margin-bottom: 8px;
  color: #333;
}

.field-description {
  font-size: 14px;
  color: #666;
  margin-bottom: 8px;
}

.form-input,
.form-textarea,
.form-select {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.form-input:focus,
.form-textarea:focus,
.form-select:focus {
  outline: none;
  border-color: #409eff;
}

.form-textarea {
  min-height: 100px;
  resize: vertical;
}

.form-switch {
  display: block;
  margin-top: 8px;
}

.submit-button {
  background-color: #409eff;
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #66b1ff;
}

.submit-button:active {
  background-color: #3a8ee6;
}
</style>