<!-- DetailsDialog.vue -->
<template>
  <el-dialog :value="isVisible" title="详细信息" :width="dialogWidth" @update:value="emitUpdate">
    <pre>{{ details }}</pre>
    <span slot="footer" class="dialog-footer">
      <el-button @click="closeDialog">关闭</el-button>
    </span>
  </el-dialog>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  details: Object,
  isVisible: Boolean,
  dialogWidth: String
});

const emit = defineEmits(['update:isVisible']);

const closeDialog = () => {
  emit('update:isVisible', false);
};

const emitUpdate = (value) => {
  emit('update:isVisible', value);
};
</script>

<style scoped>
/* 可以在这里添加样式 */
</style>
