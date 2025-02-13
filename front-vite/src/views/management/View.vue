<script setup>
import { ref } from "vue";
import SideBar from "@/views/management/layout/SideBar.vue";
import Content from "@/views/management/layout/Content.vue";

const menuItems = ref([
  { name: "dashboard", label: "仪表盘", path: "/management/dashboard", icon: "📊" },
  { name: "users", label: "学生表格", path: "/management/students", icon: "👤" },
  { name: "filter", label: "筛选", path: "/management/filter", icon: "🔍" },
  { name: "interview", label: "面试打分", path: "/management/interview", icon: "📋" },
  { name: "analytics", label: "数据分析", path: "/management/analysis", icon: "📈" },
  { name: "setting", label: "系统设置", path: "/management/setting", icon: "⚙️" },
]);
</script>
<template>
  <div class="admin-layout">
    <div class="sidebar-container">
      <SideBar :menuItems="menuItems" />
    </div>

    <div class="main-container">
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
