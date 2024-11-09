<template>
  <div class="admin-layout">
    <!-- 顶栏 -->
    <header class="admin-header">
      <div class="logo">后台管理系统</div>
      <nav class="nav-links">
        <router-link to="/dashboard" class="nav-link">仪表盘</router-link>
        <router-link to="/settings" class="nav-link">设置</router-link>
        <router-link to="/profile" class="nav-link">个人中心</router-link>
        <button @click="logout" class="logout-button">登出</button>
      </nav>
    </header>

    <!-- 主体部分 -->
    <div class="admin-body">
      <!-- 侧栏 -->
      <aside class="sidebar">
        <ul class="menu">
          <li v-for="item in menuItems" :key="item.name" class="menu-item">
            <router-link :to="item.path" class="menu-link">
              <span class="icon">{{ item.icon }}</span>
              <span class="label">{{ item.label }}</span>
            </router-link>
          </li>
        </ul>
      </aside>

      <!-- 内容区域 -->
      <main class="content">
        <router-view></router-view>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminLayout",
  data() {
    return {
      menuItems: [
        { name: "dashboard", label: "仪表盘", path: "/dashboard", icon: "📊" },
        { name: "users", label: "用户管理", path: "/users", icon: "👤" },
        { name: "settings", label: "系统设置", path: "/settings", icon: "⚙️" },
        { name: "analytics", label: "数据分析", path: "/analytics", icon: "📈" },
      ],
    };
  },
  methods: {
    logout() {
      // 登出逻辑，可以调用API或者直接跳转到登录页面
      this.$router.push("/login");
    },
  },
};
</script>

<style scoped>
.admin-layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.admin-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  color: #fff;
  padding: 10px 20px;
}

.logo {
  font-size: 20px;
  font-weight: bold;
}

.nav-links {
  display: flex;
  align-items: center;
}

.nav-link,
.logout-button {
  color: #fff;
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

.admin-body {
  display: flex;
  flex-grow: 1;
}

.sidebar {
  width: 200px;
  background-color: #2c3e50;
  color: #ecf0f1;
  padding: 20px;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.menu {
  list-style: none;
  padding: 0;
}

.menu-item {
  margin-bottom: 15px;
}

.menu-link {
  color: #ecf0f1;
  text-decoration: none;
  font-size: 18px;
  display: flex;
  align-items: center;
}

.menu-link:hover {
  color: #3498db;
}

.icon {
  margin-right: 10px;
}

.content {
  flex-grow: 1;
  padding: 20px;
  background-color: #f4f6f8;
}
</style>
