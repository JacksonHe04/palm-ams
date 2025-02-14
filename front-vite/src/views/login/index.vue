<script setup>
import Login from "@/views/login/components/Login.vue";
</script>

<template>
  <div class="login-main p-5 md:p-0">
    <Login />
  </div>
</template>

<style scoped lang="scss">
.login-main {
  width: 100%;
  min-height: calc(100vh - 10rem);
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
