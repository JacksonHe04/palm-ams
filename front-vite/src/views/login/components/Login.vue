// src/views/Login/Login.vue
<script>
import { ref } from "vue";
import { useUserStore } from "@/stores/userStore.ts";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";

export default {
  setup() {
    const username = ref("");
    const password = ref("");
    const rememberMe = ref(false);
    const userStore = useUserStore();
    const router = useRouter();

    const handleLogin = async () => {
      const loginSuccess = await userStore.login(
        username.value,
        password.value,
        rememberMe.value
      );
      
      if (loginSuccess) {
        ElMessage.success("登录成功");
        await router.push("/admin");
      } else {
        ElMessage.error("登录失败，请检查用户名和密码");
      }
    };

    return {
      username,
      password,
      rememberMe,
      handleLogin,
    };
  },
};
</script>

<template>
  <div class="login-container">
    <div class="illustration-side hidden md:flex">
      <img src="/lou.jpg" alt="Palm Logo" />
    </div>

    <div class="form-side md:w-1/2">
      <div class="logo">
        <img src="/palm_logo_cicle.png" alt="Palm Logo" />
      </div>

      <h1>Welcome back!</h1>
      <p>Please enter your details</p>

      <form class="login-form" @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="username">User Name</label>
          <input type="text" id="username" v-model="username" required />
          <!-- 使用 v-model 绑定 -->
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <div class="password-input">
            <input type="password" id="password" v-model="password" required />
            <!-- 使用 v-model 绑定 -->
            <button type="button" class="eye-icon"></button>
          </div>
        </div>

        <div class="form-row">
          <label class="remember-me">
            <input type="checkbox" v-model="rememberMe" />
            <span>Remember for 7 days</span>
          </label>
        </div>

        <button type="submit" class="login-button">Log In</button>
      </form>
    </div>

    <div class="invisible md:hidden">
      <div class="w-screen"></div>
    </div>
  </div>
</template>

<style scoped>
.login-container {
  display: flex;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 24px;
  overflow: hidden;
  margin-top: 0px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.illustration-side {
  min-width: 50%;
  flex: 1;
  align-items: center;
  justify-content: center;
  padding: 40px;
  img {
    width: 450px;
    border-radius: 24px;
  }
}

.form-side {
  background: rgba(245, 245, 245, 0.3);
  flex: 1;
  padding: 20px 80px;
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 480px;
}

.logo {
  img {
    width: 48px;
    height: 48px;
    border-radius: 100px;
  }
}

h1 {
  font-size: 32px;
  font-weight: 600;
  margin-bottom: 8px;
  color: #1a1a1a;
}

p {
  color: #666;
  margin-bottom: 12px;
}

.login-form {
  width: 100%;
}

.form-group {
  margin-bottom: 12px;
}

label {
  display: block;
  margin-bottom: 8px;
  color: #1a1a1a;
  font-weight: 500;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 12px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 0.2s;
}

input[type="text"]:focus,
input[type="password"]:focus {
  border-color: #6c63ff;
  outline: none;
}

.password-input {
  position: relative;
}

.eye-icon {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
  width: 24px;
  height: 24px;
}

.form-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.remember-me {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #1a1a1a;
}

.login-button {
  width: 100%;
  padding: 14px;
  background: #1a1a1a;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  margin-bottom: 16px;
  transition: background-color 0.2s;
}

.login-button:hover {
  background: #333;
}

.signup-prompt {
  text-align: center;
  margin: 0;
}

.signup-link {
  color: #1a1a1a;
  font-weight: 500;
  text-decoration: none;
  margin-left: 4px;
}

.signup-link:hover {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .login-container {
    flex-direction: column;
  }

  .illustration-side {
    padding: 20px;
  }

  .form-side {
    padding: 32px 24px;
  }
}
</style>
