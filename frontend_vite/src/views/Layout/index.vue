<script setup>
import LayoutHeader from "@/views/Layout/LayoutHeader.vue";
import Background from "@/views/Layout/Background.vue";
import LayoutFooter from "@/views/Layout/LayoutFooter.vue";
import BackToTop from "@/views/Layout/BackToTop.vue";
</script>

<template>
  <LayoutHeader />
  <Background>
    <slot />
    <RouterView />
  <!--  插槽-->

  </Background>
  <BackToTop />
  <LayoutFooter />
</template>
