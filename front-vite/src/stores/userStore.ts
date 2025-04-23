// userStore.js
import { defineStore } from "pinia";
import { login, getUserInfo, updateUserInfo } from "@/apis/user";
import { nextTick } from "vue";

export const useUserStore = defineStore("user", {
  state: () => ({
    isAuthenticated: false,
    user: null,
    loginTime: null,
    autoLoginDays: 7,
    userInfo: {
      phone: '',
      email: '',
    }
  }),
  getters: {
    isValidSession: (state) => {
      if (!state.isAuthenticated || !state.loginTime) return false;
      const now = new Date().getTime();
      const loginTime = new Date(state.loginTime).getTime();
      const validPeriod = state.autoLoginDays * 24 * 60 * 60 * 1000; // 转换为毫秒
      return now - loginTime < validPeriod;
    },
  },
  actions: {
    setAutoLoginDays(days) {
      this.autoLoginDays = days;
      localStorage.setItem("autoLoginDays", days.toString());
    },
    async login(username, password) {
      try {
        const response = await login(username, password);
        console.log('登录API响应:', response);
        // 修改判断逻辑，检查 response.data.success
        if (response.data && response.data.success) {
          const token = response.data.token;
          const user = response.data.user;
          // console.log('获取到的token:', token);
          // console.log('获取到的用户信息:', user);
          
          // 存储登录信息
          localStorage.setItem("token", token);
          localStorage.setItem("loginTime", new Date().toISOString());
          localStorage.setItem("user", JSON.stringify(user));
          
          // 更新状态
          this.isAuthenticated = true;
          this.user = user;
          this.loginTime = new Date().toISOString();
          
          // console.log('状态更新完成，当前状态:', {
          //   isAuthenticated: this.isAuthenticated,
          //   user: this.user,
          //   loginTime: this.loginTime
          // });
          
          // 获取用户详细信息
          await this.fetchUserInfo();
          
          await nextTick();
          return true;
        }
        return false;
      } catch (error) {
        console.error("登录失败:", error);
        return false;
      }
    },

    async fetchUserInfo() {
      try {
        const response = await getUserInfo();
        if (response.data.success) {
          const { phone, email, auto_login_days } = response.data.data;
          this.userInfo.phone = phone || '';
          this.userInfo.email = email || '';
          this.autoLoginDays = auto_login_days;
          localStorage.setItem("userInfo", JSON.stringify({ phone, email }));
          localStorage.setItem("autoLoginDays", auto_login_days.toString());
        }
      } catch (error) {
        console.error("获取用户信息失败:", error);
      }
    },

    async updateUserInfo(data) {
      try {
        const response = await updateUserInfo(data);
        if (response.data.success) {
          if (data.phone !== undefined) this.userInfo.phone = data.phone;
          if (data.email !== undefined) this.userInfo.email = data.email;
          if (data.auto_login_days !== undefined) {
            this.autoLoginDays = data.auto_login_days;
            localStorage.setItem("autoLoginDays", data.auto_login_days.toString());
          }
          localStorage.setItem("userInfo", JSON.stringify(this.userInfo));
          return true;
        }
        return false;
      } catch (error) {
        console.error("更新用户信息失败:", error);
        return false;
      }
    },

    logout() {
      // 清除状态
      this.isAuthenticated = false;
      this.user = null;
      this.loginTime = null;
      
      // 清除本地存储
      localStorage.removeItem('token');
      localStorage.removeItem('loginTime');
      localStorage.removeItem('user');
      localStorage.removeItem('autoLoginDays');
      
      // 重定向到登录页面
      window.location.href = '/login';
    },

    initializeFromStorage() {
      const token = localStorage.getItem("token");
      const loginTime = localStorage.getItem("loginTime");
      const user = localStorage.getItem("user");
      const autoLoginDays = localStorage.getItem("autoLoginDays");

      if (token && loginTime && user) {
        this.isAuthenticated = true;
        this.loginTime = loginTime;
        this.user = JSON.parse(user);
      }

      if (autoLoginDays) {
        this.autoLoginDays = parseInt(autoLoginDays);
      }
    },
  },
});
