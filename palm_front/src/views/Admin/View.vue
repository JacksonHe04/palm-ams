<script setup>
import { ref } from "vue";
import AdminHeader from "@/views/Admin/Layout/AdminHeader.vue";
import SideBar from "@/views/Admin/Layout/SideBar.vue";
import Content from "@/views/Admin/Layout/Content.vue";

const menuItems = ref([
  { name: "dashboard", label: "仪表盘", path: "/admin/dashboard", icon: "📊" },
  { name: "users", label: "学生表格", path: "/admin/students", icon: "👤" },
  { name: "interview", label: "面试打分", path: "/admin/interview", icon: "📋" },
  { name: "analytics", label: "数据分析", path: "/admin/analysis", icon: "📈" },
  { name: "setting", label: "系统设置", path: "/admin/setting", icon: "⚙️" },
]);
</script>
<template>
  <div class="admin-layout">
    <div class="sidebar-container">
      <SideBar :menuItems="menuItems" />
    </div>

    <div class="main-container">
      <div class="header-container">
        <AdminHeader />
      </div>
      <main class="content-container">
        <Content />
      </main>
    </div>
  </div>
</template>

<style scoped>
.admin-layout {
  display: flex;
  min-height: calc(100vh - 60px);
  width: 100%;
  justify-content: center;
  border: 1px solid #ccc;
}

.sidebar-container {
  width: 20%;
  display: flex;
  flex-direction: column;
}

.main-container {
  display: flex;
  flex-direction: column;
  flex-grow: 1; /* 主区域占据剩余宽度 */
}

.content-container {
  flex-grow: 1;
  padding: 0px;
}
</style>
