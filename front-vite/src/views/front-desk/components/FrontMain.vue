<script setup>
import Footer from '@/views/layout/components/Footer.vue';
</script>

<template>
  <div class="home-main my-0 md:my-8 pb-20 px-5">
    <slot />
  </div>
  <Footer />
</template>

<style scoped>
.home-main {
  max-width: 1200px;
}
</style>
