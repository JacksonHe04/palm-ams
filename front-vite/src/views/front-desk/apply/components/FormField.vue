<template>
  <div class="form-item">
    <label :for="field.variableName">{{ field.name }}</label>
    <div class="field-description">{{ field.description }}</div>

    <!-- 文本、数字、邮箱输入框 -->
    <input
      v-if="isBasicInput"
      :type="field.type"
      :id="field.variableName"
      :value="inputValue"
      :name="field.variableName"
      class="form-input"
      :required="required"
      @input="handleInput"
    />

    <!-- 百分比 -->
    <input
      v-else-if="field.variableName === 'percentage'"
      type="text"
      :id="field.variableName"
      :value="inputValue"
      :name="field.variableName"
      class="form-input"
      disabled
    />

    <!-- 文本域 -->
    <textarea
      v-else-if="field.type === 'textarea'"
      :id="field.variableName"
      :value="inputValue"
      :name="field.variableName"
      class="form-textarea"
      :required="required"
      @input="handleInput"
    ></textarea>

    <!-- 自动搜索下拉框 -->
    <AutoCompleteInput
      v-else-if="isAutoCompleteField"
      :model-value="inputValue"
      :options="options"
      :placeholder="'请输入' + field.name"
      @update:model-value="handleInput"
    />

    <!-- 普通单选下拉框 -->
    <select
      v-else-if="field.type === 'select'"
      :id="field.variableName"
      :value="inputValue"
      :name="field.variableName"
      class="form-select"
      :required="required"
      @input="handleInput"
    >
      <option value="">请选择</option>
      <option
        v-for="option in options"
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
      :model-value="inputValue"
      :name="field.variableName"
      class="form-switch"
      :required="required"
      @update:model-value="handleInput"
    />

    <!-- 奖项贡献字段 -->
    <div
      v-else-if="isContributionField"
      class="flex gap-4 items-center"
    >
      <div class="flex-1">
        <input
          type="number"
          :id="`${field.variableName}_rank`"
          v-model="contributionRank"
          class="form-input"
          placeholder="贡献排名"
          min="1"
          @input="handleContributionChange"
        />
      </div>
      <span class="text-gray-500">/</span>
      <div class="flex-1">
        <input
          type="number"
          :id="`${field.variableName}_total`"
          v-model="contributionTotal"
          class="form-input"
          placeholder="团队人数"
          min="1"
          @input="handleContributionChange"
        />
      </div>
    </div>

    <!-- 其他类型 -->
    <input
      v-else
      :type="field.type"
      :id="field.variableName"
      :value="inputValue"
      :name="field.variableName"
      class="form-input"
      :required="required"
      @input="handleInput"
    />
  </div>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { ElSwitch } from 'element-plus'
import AutoCompleteInput from './AutoCompleteInput.vue'

interface Props {
  field: {
    id: string
    name: string
    type: string
    variableName: string
    description?: string
  }
  modelValue: any
  required?: boolean
  options?: Array<{ value: string; label: string }>
  contributionData?: {
    rank: string | number
    total: string | number
  }
}

const props = withDefaults(defineProps<Props>(), {
  required: false,
  options: () => [],
  contributionData: () => ({ rank: '', total: '' })
})

const emit = defineEmits(['update:modelValue', 'input', 'contribution-change'])

/**
 * 计算属性：用于处理输入值的双向绑定
 */
const inputValue = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
})

// 计算属性
const isBasicInput = computed(() => {
  return (
    (props.field.type === 'text' ||
      props.field.type === 'number' ||
      props.field.type === 'email') &&
    props.field.variableName !== 'percentage'
  )
})

const isAutoCompleteField = computed(() => {
  return (
    props.field.type === 'select' &&
    ['本科学校', '硕士学校', '本科专业', '硕士专业'].includes(props.field.name)
  )
})

const isContributionField = computed(() => {
  return [
    'award1_contribution',
    'award2_contribution',
    'award3_contribution'
  ].includes(props.field.variableName)
})

// 贡献度相关
const contributionRank = ref(props.contributionData.rank)
const contributionTotal = ref(props.contributionData.total)

/**
 * 处理输入事件
 * @param e 输入事件或新值
 */
const handleInput = (e: Event | any) => {
  const value = e instanceof Event ? (e.target as HTMLInputElement).value : e
  emit('update:modelValue', value)
  if (e instanceof Event) {
    emit('input', e)
  }
}

/**
 * 处理贡献度变更
 */
const handleContributionChange = () => {
  // 先触发贡献度数据更新
  emit('contribution-change', {
    rank: contributionRank.value,
    total: contributionTotal.value
  })
  
  // 同时更新 v-model 绑定的值
  if (contributionRank.value && contributionTotal.value) {
    emit('update:modelValue', `${contributionRank.value}/${contributionTotal.value}`)
  } else {
    emit('update:modelValue', '')
  }
}

// 监听贡献度数据变化
watch(
  () => props.contributionData,
  (newVal) => {
    contributionRank.value = newVal.rank
    contributionTotal.value = newVal.total
  },
  { deep: true }
)
</script>

<style lang="scss" scoped>
@use "../index.scss";
.form-item {
  @apply mb-4;
  
  label {
    @apply block text-sm font-medium text-gray-700 mb-1;
  }

  .field-description {
    @apply text-sm text-gray-500 mb-2;
  }
}
</style>