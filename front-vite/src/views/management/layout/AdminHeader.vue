<!-- src/layout/AdminHeader.vue -->
<template>
  <header class="admin-header">
    <!-- 左侧占位 -->
    <div class="logo"></div>
    <nav class="nav-links">
      <RouterLink to="/admin/profile" class="nav-link">个人中心</RouterLink>
      <button @click="logout" class="logout-button">登出</button>
    </nav>
  </header>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();

const logout = () => {
  router.push("/login");
};
</script>

<style scoped>
.admin-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: white;
  color: #141414;
  padding: 10px 20px;
  border-radius: 10px;
  margin: 30px 50px 30px 30px; /* 增加外边距 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
}

.logo {
  font-size: 20px;
}

.nav-links {
  display: flex;
  align-items: center;
}

.nav-link,
.logout-button {
  color: #141414;
  font-weight: normal;
  margin-left: 15px;
  text-decoration: none;
  font-size: 16px;
}

.logout-button {
  background: transparent;
  border: none;
  cursor: pointer;
  font-size: 16px;
}
</style>
