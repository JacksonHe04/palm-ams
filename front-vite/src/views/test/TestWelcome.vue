<script setup>
import { ref } from 'vue';
import axios from 'axios';

// 定义一个响应式变量来存储后端返回的数据
const apiData = ref(null);

// 定义一个方法来调用后端API
const fetchData = async () => {
  try {
    const response = await axios.get('http://localhost:3000/api/home/welcome');
    apiData.value = response.data;
    console.log('GET请求成功:', response.data);
  } catch (error) {
    console.error('请求失败:', error);
  }
};
</script>

<template>
  <div>
    <button @click="fetchData">无参数的简单 GET 测试</button>
    <div v-if="apiData" class="pre-div">
      <pre>{{ JSON.stringify(apiData, null, 2) }}</pre>
    </div>
  </div>
</template>

<style scoped>
button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

.pre-div {
  margin-top: 30px;
  text-align: center;
}

pre {
  background-color: rgba(244, 244, 244, 0);
  display: inline-block;
  padding: 10px;
  width: fit-content;
  white-space: pre-wrap;
  word-wrap: break-word;
}
</style>
