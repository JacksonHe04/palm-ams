<template>
  <div>
    <h2>测试表单提交</h2>
    <form @submit.prevent="testFormSubmit">
      <label for="testInput">测试输入:</label>
      <input type="text" id="testInput" v-model="testInput" required>
      <button type="submit">提交</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const testInput = ref('');
let message = ref('');

const testFormSubmit = () => {
  if (testInput.value.trim() === '') {
    message.value = '输入不能为空！';
    return;
  }

  message.value = '提交成功！输入值为: ' + testInput.value;
  console.log('提交的数据:', testInput.value);
  return true; // 返回 true 表示验证通过
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  max-width: 300px;
  margin: 0 auto;
}

label {
  margin-bottom: 5px;
}

input {
  margin-bottom: 10px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
