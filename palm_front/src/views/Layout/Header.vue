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
    <div class="auth-buttons">
      <RouterLink to="/signup" class="btn btn-know">Sign Up</RouterLink>
      <RouterLink to="/login" class="btn btn-apply">Login</RouterLink>
    </div>
  </nav>
</template>

<style scoped>
/* Navigation */
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 40px 170px;
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
