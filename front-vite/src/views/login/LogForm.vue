<template>
  <div class="login-form">
    <h2>登录</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username" class="label-text">用户名</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password" class="label-text">密码</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">登录</button>
    </form>
    <p v-if="loginSuccess">登录成功！</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');
const loginSuccess = ref(false);
const router = useRouter();

const handleLogin = () => {
  if (username.value === 'management' && password.value === '123456') {
    loginSuccess.value = true;
    console.log('登录成功');
    // 登录成功后跳转到 /management
    router.push('/management');
  } else {
    loginSuccess.value = false;
    console.log('用户名或密码错误');
  }
};
</script>

<style scoped>
.login-form {
  max-width: 600px;
  margin: 150px auto;
  padding: 30px 60px;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 25%;
}

.form-group {
  margin-bottom: 20px;
}

.label-text {
  display: block;
  margin-bottom: 8px;
  font-weight: normal;
  color: #888888; /* 设置为灰色 */
  text-align: left; /* 靠左对齐 */
}

input {
  width: 100%;
  padding: 12px;
  box-sizing: border-box;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  transition: border-color 0.3s ease;
}

input:focus {
  border-color: #007bff;
  outline: none;
}

button {
  width: 100%;
  padding: 12px;
  background-color: #007bff;
  color: #ffffff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

p {
  text-align: center;
  color: #4caf50;
  font-weight: bold;
}
</style>
