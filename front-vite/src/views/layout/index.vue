<script setup>
import Background from "@/views/layout/components/Background.vue";
import Footer from "@/views/layout/components/Footer.vue";
import BackToTop from "@/views/layout/components/BackToTop.vue";
import Header from "@/views/layout/components/Header.vue";
</script>

<template>
  <Background>
    <Header />
    <div class="content">
      <RouterView />
    </div>
    <BackToTop />
    <Footer />
  </Background>
</template>

<style scoped>
.content {
  margin-top: 116px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  min-height: calc(100vh - 60px);
}
</style>
