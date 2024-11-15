<script setup>
import LayoutHeader from "@/views/Layout/LayoutHeader.vue";
import Background from "@/views/Layout/Background.vue";
import LayoutFooter from "@/views/Layout/LayoutFooter.vue";
import BackToTop from "@/views/Layout/BackToTop.vue";
</script>

<template>
  <LayoutHeader />
  <Background>
    <RouterView />
  </Background>
  <BackToTop />
  <LayoutFooter />
</template>
