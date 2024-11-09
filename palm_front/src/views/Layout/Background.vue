<template>
  <div class="hero-section">
    <div class="container">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "Background",
};
</script>

<style scoped>
.hero-section {
  position: relative;
  display: flex;
  justify-content: center;
  min-height: calc(100vh - 60px);
  background-image: linear-gradient(
      15deg,
      rgba(10, 24, 85, 0.6) 0%,
      rgba(136, 194, 213, 0.6) 100%
  );
  background-attachment: fixed;
  background-size: cover;
  overflow: hidden;
  align-items: center;
}

.container {
  position: relative;
  z-index: 1;
  text-align: center;
  margin: 0;
  width: 100%;
  padding: 0;
}
</style>
