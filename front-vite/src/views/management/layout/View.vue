<script setup>
import { ref } from "vue";
import SideBar from "@/views/management/layout/SideBar.vue";
import Content from "@/views/management/layout/Content.vue";

const isSidebarCollapsed = ref(false);

const toggleSidebar = () => {
  isSidebarCollapsed.value = !isSidebarCollapsed.value;
};
</script>

<template>
  <div class="admin-layout">
    <div :class="['sidebar-container', { collapsed: isSidebarCollapsed }]">
      <SideBar :isCollapsed="isSidebarCollapsed" @toggle="toggleSidebar" />
    </div>

    <main :class="['main-container', { expanded: isSidebarCollapsed }]">
      <Content />
    </main>
  </div>
</template>

<style scoped lang="scss">
.admin-layout {
  position: relative;
  display: flex;
  min-height: calc(100vh - 0px);
  width: 100%;
}

.sidebar-container {
  position: fixed;
  left: 0;
  height: 100%;
  width: 250px; // 展开时的宽度
  display: flex;
  flex-direction: column;
  border: $admin-border 1px solid;
  border-right: $admin-border 0.5px solid;
  transition: width 0.3s ease;

  &.collapsed {
    width: 40px; // 折叠后的宽度，仅显示按钮
  }
}

.main-container {
  position: absolute;
  left: 250px; // 展开时的左侧位置
  width: calc(100% - 250px); // 展开时的宽度
  height: 100%;
  display: flex;
  flex-direction: column;
  border: $admin-border 1px solid;
  border-left: $admin-border 0.5px solid;
  transition: left 0.3s ease, width 0.3s ease;

  &.expanded {
    left: 40px; // 折叠时的左侧位置
    width: calc(100% - 40px); // 折叠时的宽度
  }
}
</style>
