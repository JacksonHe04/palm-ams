<script setup>
import LayoutHeader from "@/views/Layout/LayoutHeader.vue";
import Background from "@/views/Layout/Background.vue";
import LayoutFooter from "@/views/Layout/LayoutFooter.vue";
import BackToTop from "@/views/Layout/BackToTop.vue";
</script>

<template>
  <Background>
    <LayoutHeader />
    <div class="content">
      <RouterView />
    </div>
    <BackToTop />
    <LayoutFooter />
  </Background>
</template>

<style scoped>
.content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  min-height: calc(100vh - 60px);
}
</style>
