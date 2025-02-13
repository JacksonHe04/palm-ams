<script setup>
import { ref } from 'vue'
import axios from 'axios'

// 学生信息表单数据
const studentForm = ref({
  name: '',
  age: '',
  grade: ''
})

// 提交表单
const handleSubmit = async () => {
  try {
    const response = await axios.post('http://localhost:3000/api/test/test_post/', studentForm.value)
    alert('学生信息提交成功')
    console.log(response.data)
  } catch (error) {
    alert('学生信息提交失败')
    console.error(error)
  }
}

// 查询学生信息
const searchStudent = ref('')
const studentInfo = ref({})

const handleSearch = async () => {
  try {
    const response = await axios.get(`http://localhost:3000/api/test/test_get/?name=${searchStudent.value}`)
    console.log('Response data:', response.data) // 添加调试信息
    studentInfo.value = response.data.data
  } catch (error) {
    alert('查询失败')
    console.error(error)
  }
}
</script>

<template>
  <div>
    <!-- 学生信息表单 -->
    <form @submit.prevent="handleSubmit">
      <label for="name">姓名:</label>
      <input id="name" v-model="studentForm.name" required />

      <label for="age">年龄:</label>
      <input id="age" v-model="studentForm.age" type="number" required />

      <label for="grade">年级:</label>
      <input id="grade" v-model="studentForm.grade" required />

      <button type="submit">提交</button>
    </form>

    <!-- 查询学生信息 -->
    <div>
      <input v-model="searchStudent" placeholder="请输入学生姓名" />
      <button @click="handleSearch">查询</button>
    </div>

    <!-- 显示查询结果 -->
    <div v-if="Object.keys(studentInfo).length > 0">
      <h3>查询结果:</h3>
      <p>姓名: {{ studentInfo.name }}</p>
      <p>年龄: {{ studentInfo.age }}</p>
      <p>年级: {{ studentInfo.grade }}</p>
    </div>
  </div>
</template>

<style scoped>
/* 样式可以根据需求调整 */
form, div {
  margin-bottom: 20px;
}
input, button {
  margin-right: 10px;
}
</style>
