<template>
  <div class="hero-section">
    <div class="container">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    // 确保 hero-section 的高度可以超过视口高度
    const heroSection = this.$el;
    heroSection.style.height = 'auto'; // 设置为 auto 以适应内容高度
    heroSection.style.minHeight = `${window.innerHeight}px`; // 确保至少有视口高度

    window.addEventListener('resize', () => {
      heroSection.style.minHeight = `${window.innerHeight}px`; // 动态调整最小高度
    });
  }
};
</script>

<style scoped>
.hero-section {
  display: flex;
  justify-content: center;
  background-image: url("/home-bg-m.png");
  background-attachment: fixed;
  background-size: cover;
  overflow: hidden; /* 允许垂直滚动 */
  align-items: center;
  position: relative; /* 确保子元素的绝对定位相对于 hero-section */
  height: auto; /* 设置为 auto 以适应内容高度 */
}

.container {
  max-width: unset;
  position: relative;
  z-index: 1;
  text-align: center;
  margin: 0;
  width: 100%;
  padding: 0;
  overflow: hidden; /* 不需要内部滚动，内容会自动溢出到 hero-section */
}
</style>