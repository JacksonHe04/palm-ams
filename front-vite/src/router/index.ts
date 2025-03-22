import { createRouter, createWebHistory } from "vue-router";
import { useUserStore } from "@/stores/userStore";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      component: () => import("@/views/layout/index.vue"),
      children: [
        {
          path: "/:pathMatch(.*)*",
          component: () => import("@/views/front-desk/404/index.vue"),
          meta: { title: "404 Not Found" },
        },
        {
          path: "",
          component: () => import("@/views/front-desk/home/index.vue"),
          meta: { title: "欢迎申请 PALM 实验室！" },
        },
        {
          path: "/apply",
          component: () => import("@/views/front-desk/new_apply/index.vue"),
          meta: { title: "申请 PALM 实验室" },
        },
        // /wait
        {
          path: "/wait",
          component: () => import("@/views/front-desk/wait/index.vue"),
          meta: { title: "申请提交成功，请等待回复" },
        },
        {
          path: "/login",
          component: () => import("@/views/login/index.vue"),
          meta: { title: "登录 PALM 实验室" },
        },
        {
          path: "/admin",
          redirect: "/admin/result",
          component: () => import("@/views/management/index.vue"),
          meta: { title: "PALM实验室后台管理" },
          children: [
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
            {
              path: "percent",
              component: () => import("@/views/management/percent/index.vue"),
              meta: { title: "百分比" },
            },
            {
              path: "result",
              name: "result",
              component: () => import("@/views/management/result/index.vue"),
              meta: { title: "录取结果" },
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
            {
              path: "field",
              name: "field",
              component: () => import("@/views/management/field/index.vue"),
              meta: { title: "字段配置" },
            },
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
          component: () => import("@/views/front-desk/about/index.vue"),
          meta: { title: "关于开发者" },
        },
        {
          path: "/read",
          component: () => import("@/views/front-desk/read/index.vue"),
          meta: { title: "PALM实验室申请说明" },
        },
        {
          path: "/introduction",
          component: () => import("@/views/front-desk/introduction/index.vue"),
          meta: { title: "PALM实验室介绍" },
        },
        {
          path: "/news",
          component: () => import("@/views/front-desk/news/index.vue"),
          meta: { title: "PALM实验室新闻" },
        },
        {
          path: "/members",
          component: () => import("@/views/front-desk/members/index.vue"),
          meta: { title: "PALM实验室成员" },
        },
        {
          path: "/academics",
          component: () => import("@/views/front-desk/academics/index.vue"),
          meta: { title: "PALM实验室学术" },
        },
        {
          path: "/test",
          component: () => import("@/views/test/index.vue"),
          meta: { title: "开发者测试页面" },
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

// 全局前置守卫
router.beforeEach((to, from, next) => {
  const userStore = useUserStore();
  const isAdminRoute = to.path.startsWith('/admin');

  // 初始化用户状态
  userStore.initializeFromStorage();

  if (isAdminRoute) {
    // 检查是否是有效的登录会话
    if (userStore.isValidSession) {
      next();
    } else {
      // 未登录或会话过期，重定向到登录页
      next('/login');
    }
  } else {
    // 非管理员路由，直接放行
    next();
  }
});

export default router;
