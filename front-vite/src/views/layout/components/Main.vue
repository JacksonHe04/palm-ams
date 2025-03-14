<template>
  <div class="main mt-14 md:mt-16">
    <RouterView />
  </div>
</template>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: calc(100vh - 4.5rem);
}
</style>
