<template>
  <div v-show="isVisible" class="scroll-to-top" @click="scrollToTop">
    <!-- 使用 CSS 绘制向上的等腰三角形 -->
    <div class="arrow-up"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isVisible: false, // 控制按钮是否可见
    };
  },
  mounted() {
    // 监听滚动事件，判断是否显示按钮
    window.addEventListener("scroll", this.toggleVisibility);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.toggleVisibility);
  },
  methods: {
    toggleVisibility() {
      // 当滚动超过一定距离时显示按钮
      this.isVisible = window.scrollY > 20;
    },
    scrollToTop() {
      // 使用 window.scrollTo 平滑滚动到顶部
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    },
  },
};
</script>

<style scoped>
/* 固定位置在右下角，设置圆形按钮的样式 */
.scroll-to-top {
  position: fixed;
  bottom: 40px;
  right: 40px;
  width: 50px;
  height: 50px;
  background-color: #fff;
  border-radius: 50%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999; /* 确保在最顶层 */
  cursor: pointer;
}

.arrow-up {
  display: inline-block;
  margin-top: 13px;
  border-top: 2px solid;
  border-right: 2px solid;
  border-bottom: 4px solid transparent;
  border-left: 4px solid transparent;
  width: 20px;
  height: 20px;
  transform: rotate(-45deg);
  color: #b4cbb5;
}
</style>
