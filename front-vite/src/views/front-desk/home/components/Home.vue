<template>
  <div class="container">
    <HeroSection />
    <HomeCards />
  </div>
</template>

<script setup>
import HeroSection from "./HeroSection.vue";
import HomeCards from "./HomeCards.vue";
</script>

<style scoped lang="scss">
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, sans-serif;
}

body {
  background: url("/home-bg.jpg") no-repeat center center fixed;
  background-size: cover;
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .container {
    padding: 0 16px;
  }
}
</style>
