// userStore.js
import { defineStore } from "pinia";
import { login } from "@/apis/user";
import { nextTick } from "vue";

export const useUserStore = defineStore("user", {
  state: () => ({
    isAuthenticated: false,
    user: null,
  }),
  actions: {
    async login(username, password) {
      try {
        const response = await login(username, password);
        console.log("Response:", response); // 打印响应内容
        if (response.status >= 200 && response.status < 300) {
          const token = response.data.token || "default_token"; // 如果后端不返回 token，请调整此处
          localStorage.setItem("token", token); // 存储 token
          this.isAuthenticated = true;
          this.user = response.data.user; // 假设后端返回的用户信息在 response.data.user 中
          console.log("State after login:", this.$state); // 打印当前状态
          await nextTick(); // 确保状态更新完成

          // 不再在这里获取路由器实例，而是返回一个标志
          return true;
        } else {
          console.error("Unexpected status code:", response.status);
        }
      } catch (error) {
        console.error("登录失败:", error);
        console.log("Error Response:", error.response); // 打印错误响应内容
      }
      return false;
    },
  },
});
