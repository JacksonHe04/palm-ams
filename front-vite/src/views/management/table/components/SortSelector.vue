<!-- SortSelector.vue -->
<template>
  <div class="form-setting form-sort">
    <el-select v-model="selectedSort" placeholder="排序" @change="onSortChange">
      <el-option
        v-for="option in sortOptions"
        :key="option.value"
        :label="option.label"
        :value="option.value"
      />
    </el-select>
  </div>
</template>

<script setup>
import { ref, computed, watch } from "vue";
import { useStudentsStore } from "@/stores/studentsStore.js";

const store = useStudentsStore();

// 接收父组件传递的 props
const props = defineProps({
  fields: {
    type: Array,
    required: true,
  },
  onSortChange: {
    type: Function,
    required: true,
  },
});

// 计算属性
const sortOptions = computed(() => {
  return props.fields.map((field) => ({
    label: field,
    value: field,
  }));
});

// 排序字段
const selectedSort = ref("ID"); // 初始化默认排序字段

// 监听排序字段变化
watch(selectedSort, (newVal) => {
  props.onSortChange(newVal);
});
</script>

<style scoped lang="scss">
.form-setting {
  height: 100%;
  flex: 1;
}
.form-sort {
  width: 25%;
}
</style>
