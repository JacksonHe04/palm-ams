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
      <button class="btn btn-ghost">Sign Up</button>
      <button class="btn btn-primary">Login</button>
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
  font-weight: 600;
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
  color: #1f2937;
}

.auth-buttons {
  display: flex;
  gap: 16px;
}

.btn {
  padding: 8px 16px;
  border-radius: 6px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-ghost {
  background: transparent;
  border: 1px solid #000000;
}

.btn-primary {
  background: #1f2937;
  color: white;
  border: none;
}
</style>
