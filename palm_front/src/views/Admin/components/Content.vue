<script setup>
import { ref } from 'vue';

const contentRef = ref(null);

let isDragging = false;
let startY;
let scrollTop;

const startDragging = (e) => {
  isDragging = true;
  startY = e.pageY - contentRef.value.offsetTop;
  scrollTop = contentRef.value.scrollTop;
};

const stopDragging = () => {
  isDragging = false;
};

const drag = (e) => {
  if (!isDragging) return;
  e.preventDefault();
  const y = e.pageY - contentRef.value.offsetTop;
  const walk = (y - startY) * 1.5; // 拖动速度
  contentRef.value.scrollTop = scrollTop - walk;
};

window.addEventListener('mouseup', stopDragging);
window.addEventListener('mouseleave', stopDragging);
</script>

<template>
  <div
    class="content"
    ref="contentRef"
    @mousedown="startDragging"
    @mousemove="drag"
  >
    <RouterView />
  </div>
</template>

<style scoped>
.content {
  background-color: white;
  border-radius: 10px;
  margin: 0px 50px 0px 30px; /* 增加外边距 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  height: calc(100% - 30px);
  padding: 0;
  overflow-y: auto; /* 允许垂直滚动 */
  overflow-x: scroll; /* 允许水平滚动 */
  white-space: nowrap; /* 防止内容换行 */
  width: 1100px; /* 固定宽度 */
}
</style>
