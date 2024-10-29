<script setup>
import Hello from "./components/Hello.vue";
import ApplyView from "./components/ApplyView.vue";
import SimpleButton from "./components/SimpleButton.vue";

// import comTest from "./components/comTest.vue";
</script>

<template>
  <div id="app">
    <ApplyView />
    <SimpleButton />
  </div>
</template>

<style scoped>#app {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
</style>
