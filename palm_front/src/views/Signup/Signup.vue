<template>
  <div class="login-container">
    <div class="illustration-side">
      <img src="/lou.jpg" alt="Palm Logo" />
    </div>

    <div class="form-side">
      <div class="logo">
        <img src="/palm_logo.png" alt="Palm Logo" />
      </div>

      <h1>Let's Take it</h1>
      <p>Please enter your registration details</p>

      <form class="login-form" @submit.prevent="handleRegister">
        <div class="form-group">
          <label for="username">User Name</label>
          <input type="text" id="username" v-model="username" required />
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <div class="password-input">
            <input
              :type="passwordFieldType"
              id="password"
              v-model="password"
              required
            />
            <button
              type="button"
              class="eye-icon"
              @click="togglePasswordVisibility"
            ></button>
          </div>
        </div>

        <div class="form-row">
          <label class="remember-me">
            <input type="checkbox" v-model="rememberMe" />
            <span>Remember for 30 days</span>
          </label>
        </div>

        <button type="submit" class="login-button">Sign Up</button>
        <p class="signup-prompt">
          You already have an account?
          <RouterLink to="/login" class="signup-link">Log In</RouterLink>
        </p>

        <!-- 显示错误或成功消息 -->
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
        <p v-if="successMessage" class="success-message">
          {{ successMessage }}
        </p>
      </form>
    </div>
  </div>
</template>

<script>
import { register } from "@/apis/user";

export default {
  data() {
    return {
      username: "",
      password: "",
      rememberMe: false,
      passwordFieldType: "password",
      errorMessage: "",
      successMessage: "",
    };
  },
  methods: {
    togglePasswordVisibility() {
      this.passwordFieldType =
        this.passwordFieldType === "password" ? "text" : "password";
    },
    async handleRegister() {
      try {
        const response = await register(this.username, this.password);

        // 处理成功响应
        this.successMessage = response.data.message;
        this.errorMessage = "";
        // 可以重定向到登录页面或其他页面
        // this.$router.push('/login');
      } catch (error) {
        // 处理错误响应
        this.errorMessage = error.response
          ? error.response.data.message
          : "Registration failed";
        this.successMessage = "";
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  display: flex;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 24px;
  overflow: hidden;
  margin-top: -100px;
  /* 阴影 */
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.illustration-side {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  img {
    width: 400px;
    height: 400px;
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
<script setup></script>
