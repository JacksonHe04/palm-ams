<template>
  <div>
    <h2>表单组件A</h2>
    <div>
      <label for="inputB">子组件B:</label>
      <B v-model="inputB" id="inputB" />
    </div>
    <div>
      <label for="inputC">子组件C:</label>
      <C v-model="inputC" id="inputC" />
    </div>
    <button @click="handleSubmit">提交</button>
  </div>
</template>

<script>
import B from "./B.vue";
import C from "./C.vue";

export default {
  components: { B, C },
  data() {
    return {
      inputB: "",
      inputC: "",
    };
  },
  methods: {
    handleSubmit() {
      console.log("inputb: ", this.inputB);
      console.log("inputC: ", this.inputC);
    },
  },
};
</script>