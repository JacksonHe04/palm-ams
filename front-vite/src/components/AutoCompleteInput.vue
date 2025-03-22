<template>
  <div class="autocomplete-container">
    <input
      type="text"
      v-model="inputValue"
      :placeholder="placeholder"
      class="form-input" 
      @input="handleInput"
      @focus="showSuggestions = true"
      @blur="handleBlur"
    />
    <div v-show="showSuggestions && filteredOptions.length > 0" class="suggestions-container">
      <div
        v-for="option in filteredOptions"
        :key="option.value"
        class="suggestion-item"
        @mousedown="selectOption(option)"
      >
        {{ option.label }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'

const props = defineProps<{
  modelValue: string
  options: Array<{ value: string; label: string }>
  placeholder?: string
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()

const inputValue = ref(props.modelValue)
const showSuggestions = ref(false)

// 监听 modelValue 的变化
watch(() => props.modelValue, (newValue) => {
  inputValue.value = newValue
})

const filteredOptions = computed(() => {
  if (!inputValue.value) return props.options
  const searchText = inputValue.value.toLowerCase()
  return props.options.filter(option => 
    option.label.toLowerCase().includes(searchText) ||
    option.value.toLowerCase().includes(searchText)
  )
})

const handleInput = () => {
  emit('update:modelValue', inputValue.value)
  showSuggestions.value = true
}

const selectOption = (option: { value: string; label: string }) => {
  inputValue.value = option.value
  emit('update:modelValue', option.value)
  showSuggestions.value = false
}

const handleBlur = () => {
  // 延迟关闭建议列表，确保点击事件能够触发
  setTimeout(() => {
    showSuggestions.value = false
  }, 200)
}
</script>

<style scoped>
.autocomplete-container {
  position: relative;
  width: 100%;
}

/* 与 index.vue 保持一致的输入框样式 */
.form-input {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.form-input:focus {
  outline: none;
  border-color: #409eff;
}

.suggestions-container {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  max-height: 200px;
  overflow-y: auto;
  background: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  z-index: 1000;
  margin-top: 4px;
}

.suggestions-container::-webkit-scrollbar {
  width: 6px;
}

.suggestions-container::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 3px;
}

.suggestions-container::-webkit-scrollbar-thumb {
  background: #c1c1c1;
  border-radius: 3px;
}

.suggestions-container::-webkit-scrollbar-thumb:hover {
  background: #a8a8a8;
}

.suggestion-item {
  padding: 8px 12px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.suggestion-item:hover {
  background-color: #f5f7fa;
}
</style>