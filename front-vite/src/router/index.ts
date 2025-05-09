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
        // home
        {
          path: "/home",
          component: () => import("@/views/front-desk/home/index.vue"),
          meta: { title: "欢迎申请 PALM 实验室！" },
        },
        // join
        {
          path: "/join",
          component: () => import("@/views/front-desk/join/index.vue"),
          meta: { title: "加入 PALM 实验室" },
        },
        // apply
        {
          path: "/apply",
          component: () => import("@/views/front-desk/apply/index.vue"),
          children: [
            // remmmend-master
            {
              path: "recommend-master",
              component: () => import("@/views/front-desk/apply/recommend-master/index.vue"),
              meta: { title: "推免申请通道" },
            },
            // exam-master
            {
              path: "exam-master",
              component: () => import("@/views/front-desk/apply/exam-master/index.vue"),
              meta: { title: "考研申请通道" },
            },
            // phd
            {
              path: "phd",
              component: () => import("@/views/front-desk/apply/phd/index.vue"),
              meta: { title: "博士申请通道" },
            },
            // direct-phd
            {
              path: "direct-phd",
              component: () => import("@/views/front-desk/apply/direct-phd/index.vue"),
              meta: { title: "直博申请通道" },
            },
          ]
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
            // database
            {
              path: "database",
              name: "database",
              component: () => import("@/views/management/database/index.vue"),
              meta: { title: "数据库" },
            },
            // dashboard
            {
              path: "dashboard",
              name: "dashboard",
              component: () => import("@/views/management/dashboard/index.vue"),
              meta: { title: "仪表盘" },
            },
            {
              path: "table",
              name: "table",
              component: () => import("@/views/management/table/index.vue"),
              meta: { title: "学生表格（旧）" },
            },
            // students
            {
              path: "students",
              component: () => import("@/views/management/students/index.vue"),
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
            // failed
            {
              path: "failed",
              name: "failed",
              component: () => import("@/views/management/failed/index.vue"),
              meta: { title: "录取失败" },
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
          path: "/contact",
          component: () => import("@/views/front-desk/contact/index.vue"),
          meta: { title: "联系我们" },
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
        // {
        //   path: "/test",
        //   component: () => import("@/views/test/index.vue"),
        //   meta: { title: "开发者测试页面" },
        // },
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

// 添加全局路由守卫
router.beforeEach(async (to, from, next) => {
  const userStore = useUserStore();
  
  // 如果是首次加载，尝试从localStorage恢复用户状态
  if (!userStore.isInitialized) {
    await userStore.initializeFromStorage();
  }
  
  // 需要登录的路由
  const requiresAuth = to.path.startsWith('/admin');
  
  if (requiresAuth) {
    // 检查是否登录且会话有效
    if (userStore.isAuthenticated && userStore.isValidSession) {
      next();
    } else {
      // 防止无限重定向循环
      if (to.path !== '/login') {
        next('/login');
      } else {
        next();
      }
    }
  } else {
    // 如果已登录且会话有效，访问登录页时重定向到管理页面
    if (to.path === '/login' && userStore.isAuthenticated && userStore.isValidSession) {
      next('/admin');
    } else {
      next();
    }
  }
});

export default router;
