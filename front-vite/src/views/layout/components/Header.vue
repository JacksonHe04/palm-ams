<template>
  <nav>
    <RouterLink to="/"><div class="logo">SEU PALM Lab</div></RouterLink>
    <div class="nav-links">
      <RouterLink to="/introduction">Introduction</RouterLink>
      <RouterLink to="/news">News</RouterLink>
      <RouterLink to="/members">Members</RouterLink>
      <RouterLink to="/academics">Academics</RouterLink>
      <RouterLink to="/read">2025 Join Us</RouterLink>
    </div>
    <div class="auth-buttons invisible">
      <RouterLink to="/signup" class="btn btn-know">Sign Up</RouterLink>
      <RouterLink to="/login" class="btn btn-apply">Login</RouterLink>
    </div>
  </nav>
</template>

<style scoped>
nav {
  position: fixed; /* 设置为固定位置 */
  top: 0; /* 距离顶部0像素 */
  left: 0; /* 距离左侧0像素 */
  width: 100%; /* 宽度占满整个屏幕 */
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 30px 170px;
  /* background-color: #fff; !* 添加背景颜色，防止内容被遮挡 *! */
  background-image: url("/home-bg-m.png");
  z-index: 1000; /* 确保导航栏在最上层 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 24px;
  font-weight: bold;
  color: #1f2937;
}

a:hover {
  text-decoration: none;
}

.nav-links {
  display: flex;
  gap: 32px;
}

.nav-links a {
  text-decoration: none;
  color: #4b5563;
  transition: color 0.3s;
}

.nav-links a:hover {
  color: #1f2937; /* 保持原有hover颜色 */
}

.auth-buttons {
  display: flex;
  gap: 16px;
  height: 30px;
}

.btn {
  padding: 2px 12px;
  border-radius: 6px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-know {
  background: transparent;
  border: 1px solid #000000;
  color: black;
}

.btn-know:hover {
  background: rgba(255, 255, 255, 0.5);
  color: black;
}

.btn-apply {
  background: black;
  color: white;
  border: none;
}

.btn-apply:hover {
  background: skyblue;
}
</style>
