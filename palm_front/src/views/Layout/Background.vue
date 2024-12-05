<template>
  <div class="hero-section">
    <div class="container">
      <slot></slot>
    </div>
  </div>
</template>

<style scoped>
.hero-section {
  position: relative;
  display: flex;
  justify-content: center;
  /* min-height: calc(100vh - 60px); */
  background-image: linear-gradient(3deg, rgb(235 239 240) 0%, rgba(173, 216, 230, 0.6) 100%);
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

