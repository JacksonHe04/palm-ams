<script setup>
import B from "./B.vue";
import C from "./C.vue";

import { useApplyStore } from "@/stores/applyStore.js";
import { submitApplication } from "@/apis/apply";
import { watch } from "vue";

const applyStore = useApplyStore();

const inputB = applyStore.inputB;
const inputC = applyStore.inputC;

watch(inputB, (newValue) => {
  applyStore.updateInputB(newValue);
});

watch(inputC, (newValue) => {
  applyStore.updateInputC(newValue);
});

const handleSubmit = async () => {
  const data = {
    inputB: applyStore.inputB,
    inputC: applyStore.inputC,
  };

  try {
    const response = await submitApplication(data);
    console.log("提交成功:", response.data);
    applyStore.resetInputs();
  } catch (error) {
    console.error("提交失败:", error);
  }
};
</script>

<template>
  <div>
    <h2>表单组件A</h2>
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="inputB">子组件B:</label>
        <B v-model="inputB" id="inputB" />
      </div>
      <div>
        <label for="inputC">子组件C:</label>
        <C v-model="inputC" id="inputC" />
      </div>
      <button type="submit">提交</button>
    </form>
  </div>
</template>
