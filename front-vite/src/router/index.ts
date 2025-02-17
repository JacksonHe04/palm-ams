import { createRouter, createWebHistory } from "vue-router";
import Login from "@/views/login/index.vue";
import Layout from "@/views/layout/index.vue";
import Home from "@/views/front-desk/home/index.vue";
import Admin from "@/views/management/index.vue";
import Apply from "@/views/apply/index.vue";
import About from "@/views/front-desk/about/index.vue";
import Test from "@/views/test/index.vue";

// const hash = createWebHashHistory();
// 不要哈希
const hash = createWebHistory();
const router = createRouter({
  history: hash,
  routes: [
    {
      path: "/",
      component: Layout,
      children: [
        {
          path: "",
          component: Home,
          meta: { title: "欢迎申请 PALM 实验室！" },
        },
        {
          path: "/apply",
          component: Apply,
          meta: { title: "申请 PALM 实验室" },
        },
        {
          path: "/login",
          component: Login,
          meta: { title: "登录PALM实验室" },
        },
        {
          path: "/admin",
          redirect: "/admin/dashboard",
          component: Admin,
          meta: { title: "PALM实验室后台管理" },
          children: [
            {
              path: "",
              name: "management-front-desk",
              component: () => import("@/views/management/dashboard/index.vue"),
              meta: { title: "PALM实验室后台管理" },
            },
            {
              path: "dashboard",
              name: "dashboard",
              component: () => import("@/views/management/dashboard/index.vue"),
              meta: { title: "仪表盘" },
            },
            {
              path: "students",
              name: "students",
              component: () => import("@/views/management/table/index.vue"),
              meta: { title: "学生表格" },
            },
            // filter
            {
              path: "filter",
              name: "filter",
              component: () => import("@/views/management/filter/index.vue"),
              meta: { title: "筛选器" },
            },
            // filtered
            {
              path: "filtered",
              name: "filtered",
              component: () => import("@/views/management/filtered/index.vue"),
              meta: { title: "筛选器" },
            },
            {
              path: "interview",
              name: "interview",
              component: () => import("@/views/management/interview/index.vue"),
              meta: { title: "面试打分" },
            },
            {
              path: "analysis",
              name: "analysis",
              component: () => import("@/views/management/analysis/index.vue"),
              meta: { title: "数据分析" },
            },
            {
              path: "setting",
              name: "setting",
              component: () => import("@/views/management/setting/index.vue"),
              meta: { title: "规则设置" },
            },
          //   字段配置
            {
              path: "field",
              name: "field",
              component: () => import("@/views/management/field/index.vue"),
              meta: { title: "字段配置" },
            },
          //   account
            {
              path: "account",
              name: "account",
              component: () => import("@/views/management/account/index.vue"),
              meta: { title: "账号管理" },
            },
          ],
        },
        {
          path: "/about",
          component: About,
          meta: { title: "关于开发者" },
        },
        {
          path: "/test",
          component: Test,
          meta: { title: "开发者测试页面" },
        },
      //   read
        {
          path: "/read",
          component: () => import("@/views/front-desk/read/index.vue"),
          meta: { title: "PALM实验室申请说明" },
        },
      //   introduction
        {
          path: "/introduction",
          component: () => import("@/views/front-desk/introduction/index.vue"),
          meta: { title: "PALM实验室介绍" },
        },
      //   news
        {
          path: "/news",
          component: () => import("@/views/front-desk/news/index.vue"),
          meta: { title: "PALM实验室新闻" },
        },
      //   members
        {
          path: "/members",
          component: () => import("@/views/front-desk/members/index.vue"),
          meta: { title: "PALM实验室成员" },
        },
      //   academics
        {
          path: "/academics",
          component: () => import("@/views/front-desk/academics/index.vue"),
          meta: { title: "PALM实验室学术" },
        },
      //   login
        {
          path: "/login",
          component: () => import("@/views/login/index.vue"),
          meta: { title: "PALM 实验室登录" },
        },
      ],
    },
  ],
  // 路由滚动行为定制
  scrollBehavior() {
    return {
      top: 0,
    };
  },
});

import { isAuthenticated } from "@/utils/auth.ts"; // 根据实际情况导入

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'palm';

  // 检查目标路由是否是 /management 或其子路由
  if (to.path.startsWith('/management')) {
    // 如果用户未登录，则重定向到 /login
    if (!isAuthenticated()) {
      next('/login');
    } else {
      // 如果用户已登录，则继续访问 /management
      next();
    }
  } else {
    // 对于其他路由，直接放行
    next();
  }
});


export default router;
