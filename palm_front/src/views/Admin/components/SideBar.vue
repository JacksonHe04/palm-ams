<template>
  <aside class="sidebar">
    <ul class="menu">
      <li v-for="item in menuItems" :key="item.name" class="menu-item">
        <RouterLink :to="item.path" class="menu-link">
          <span class="icon">{{ item.icon }}</span>
          <span class="label">{{ item.label }}</span>
        </RouterLink>
      </li>
    </ul>
  </aside>
</template>

<script setup>
import { defineProps } from 'vue';
const props = defineProps({
  menuItems: {
    type: Array,
    required: true,
  },
});
</script>

<style scoped>
.sidebar {
  background-color: white;
  color: #141414;
  padding: 20px;
  display: flex;
  flex-direction: column;
  height: 100%;
  border-radius: 10px;
  margin: 30px 0px 30px 50px; /* 增加外边距 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
}

.label {
  color: #141414;
  font-weight: normal;
}

.menu {
  list-style: none;
  padding: 0;
}

.menu-item {
  margin-bottom: 15px;
}

.menu-link {
  color: #141414;
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
</style>

