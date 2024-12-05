import '@/assets/main.css'
import { createApp } from 'vue'
import router from './router'
import { createPinia } from 'pinia';
import App from './App.vue';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css'; // Element Plus 样式
import zhCn from 'element-plus/es/locale/lang/zh-cn'; // 设置中文语言包

const app = createApp(App);

// 创建 Pinia 实例并挂载
const pinia = createPinia();
app.use(pinia);
app.use(router);

// 使用 Element Plus 并设置语言
app.use(ElementPlus, { locale: zhCn });
app.mount('#app')