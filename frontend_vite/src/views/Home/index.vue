<template>
  <div class="home">
    <Welcome />
  </div>
</template>

<script>
import Welcome from './Welcome.vue';
export default {
  name: 'Home',
  components: {
    Welcome,
  },
};
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

a:hover {
  color: #5d7faa;
  text-decoration: none;
}
</style>
