<template>
  <nav class="bg-cover bg-center" :style="navStyle">
    <div class="container mx-auto flex justify-between items-center py-3 md:py-4">
      <RouterLink to="/" class="flex items-center gap-2 text-2xl font-bold text-gray-800">
        <img src="/palm_logo_cicle.png" alt="Palm Logo" class="logo">
        <div class="nav-title">SEU PALM Lab</div>
      </RouterLink>

      <div class="hidden md:flex space-x-8">
        <RouterLink
          v-for="item in navItems"
          :key="item.to"
          :to="item.to"
          class="text-gray-600 hover:text-gray-800"
        >
          {{ item.name }}
        </RouterLink>
      </div>

      <div class="md:hidden">
        <button @click="toggleMenu" class="text-gray-600 hover:text-gray-800">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
          </svg>
        </button>
      </div>
    </div>

    <div v-if="isMenuOpen" class="md:hidden bg-transparent py-4 px-4 space-y-4">
      <RouterLink
        v-for="item in navItems"
        :key="item.to"
        :to="item.to"
        class="block text-gray-600 hover:text-gray-800"
      >
        {{ item.name }}
      </RouterLink>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useSettingStore } from '@/stores/settingStore';

const route = useRoute();
const isMenuOpen = ref(false);

// 获取设置store实例
const settingStore = useSettingStore();
// 当前招生年份
const currentAdmissionYear = ref('');

// 初始化时获取年份数据
onMounted(async () => {
  await settingStore.fetchYear();
  currentAdmissionYear.value = settingStore.year.year;
  // console.log(currentAdmissionYear.value);
});

const navStyle = computed(() => {
  return route.path.startsWith('/admin')
    ? { backgroundColor: 'white' }
    : { backgroundImage: "url('/home-bg-m.png')" };
});

// 将navItems改为计算属性，使其响应式更新
const navItems = computed(() => [
  { name: 'Introduction', to: '/introduction' },
  { name: 'News', to: '/news' },
  { name: 'Members', to: '/members' },
  { name: 'Academics', to: '/academics' },
  // 动态获取年份
  { name: `${currentAdmissionYear.value} Join Us`, to: '/read' },
]);

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};
</script>

<style scoped lang="scss">
nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.nav-title {
  color: $title-color;
}

.logo {
  display: flex;
  gap: 16px;
  height: 30px;
}

.md\:hidden {
  transition: all 2s ease;
}
</style>
