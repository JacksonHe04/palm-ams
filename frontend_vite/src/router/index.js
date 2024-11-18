import {
  createRouter,
  createWebHistory,
  createWebHashHistory,
} from "vue-router";
import { useMutitabsStore } from "@/store/mutitabs";
import { setStorage, getStorage } from "@/utils/util";
// 进度条
import NProgress from "nprogress";
import "nprogress/nprogress.css";
import "../assets/css/nprogress.scss";
// 自定义样式
// 简单配置
NProgress.inc(0.4);
NProgress.configure({ easing: "ease", speed: 500, showSpinner: true });

const routes = [
  {
    path: "/",
    name: "root",
    component: () => import("../views/Layout/index.vue"),
    hidden: true,
    meta: {
      requireAuth: false,
      index: "/",
    },
    children: [
      {
        path: "",
        component: () => import("../views/Home/index.vue"),
        meta: { title: "欢迎来到PALM实验室" }, // 页面标题
      },
      {
        path: "/home",
        component: () => import("../views/Home/index.vue"),
        meta: { title: "欢迎来到PALM实验室" }, // 页面标题
      },
      {
        path: "/apply",
        component: () => import("../views/Apply/index.vue"),
        meta: { title: "申请PALM实验室" }, // 页面标题
      },
      {
        path: "/about",
        component: () => import("../views/About/index.vue"),
        meta: { title: "关于开发者" }, // 页面标题
      },
      {
        path: "/test",
        component: () => import("../views/Test/index.vue"),
        meta: { title: "开发者测试页面" }, // 页面标题
      },
      {
        path: "/login",
        name: "login",
        component: () => import("../views/login.vue"),
        hidden: true, // 是否在侧边栏显示
        meta: {
          requireAuth: false, // 是否需要登录验证
          index: "/admin", // 默认跳转路径
        },
      },
      {
        path: "/404",
        name: "404",
        component: () => import("../views/Home/index.vue"),
        hidden: true, // 是否在侧边栏显示
        meta: {
          requireAuth: false, // 是否需要登录验证
          index: "/404", // 默认跳转路径
        },
      },
      {
        path: "/lyterminal",
        name: "lyterminal",
        component: () => import("../views/lyterminal.vue"),
        hidden: true, // 是否在侧边栏显示
        meta: {
          requireAuth: true, // 是否需要登录验证
          index: "/lyterminal", // 默认跳转路径
        },
      },
      {
        path: "index",
        name: "index",
        component: () => import("../views/index.vue"),
        iconCls: "el-icon-tickets", // 图标类名
        meta: {
          requireAuth: false, // 是否需要登录验证
          index: "/index", // 默认跳转路径
        },
        children: [
          // 超管
          // frontend_vite/src/views/dashBoard/analysis.vue
          {
            path: "/analysis",
            name: "analysis",
            component: () => import("../views/dashBoard/analysis.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/analysis", // 默认跳转路径
            },
          },
          {
            path: "/adminManage",
            name: "adminManage",
            component: () => import("../views/adminManage/adminManage.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/adminManage", // 默认跳转路径
            },
          },
          {
            path: "/userManage",
            name: "userManage",
            component: () => import("../views/userManage/userManage.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/userManage", // 默认跳转路径
            },
          },
          {
            path: "/userManageCrud",
            name: "userManageCrud",
            component: () => import("../views/userManage/userManageCrud.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/userManageCrud", // 默认跳转路径
            },
          },
          {
            path: "/carouselSettingsimg",
            name: "carouselSettingsimg",
            component: () =>
              import("../views/platformSettings/carouselSettingsimg.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/carouselSettingsimg", // 默认跳转路径
            },
          },
          {
            path: "/platformSettingsother",
            name: "platformSettingsother",
            component: () =>
              import("../views/platformSettings/platformSettingsother.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/platformSettingsother", // 默认跳转路径
            },
          },

          {
            path: "/userFeekback",
            name: "userFeekback",
            component: () => import("../views/userFeekback/userFeekback.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/userFeekback", // 默认跳转路径
            },
          },
          // 系统管理
          {
            path: "/departmentManage",
            name: "departmentManage",
            component: () =>
              import(
                "../views/systemManage/departmentManage/departmentManage.vue"
              ),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/departmentManage", // 默认跳转路径
            },
          },
          {
            path: "/menuManage",
            name: "menuManage",
            component: () =>
              import("../views/systemManage/menuManage/menuManage.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/menuManage", // 默认跳转路径
            },
          },

          {
            path: "/roleManage",
            name: "roleManage",
            component: () =>
              import("../views/systemManage/roleManage/roleManage.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/roleManage", // 默认跳转路径
            },
          },

          {
            path: "/authorityManage",
            name: "authorityManage",
            component: () =>
              import(
                "../views/systemManage/authorityManage/authorityManage.vue"
              ),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/authorityManage", // 默认跳转路径
            },
          },
          {
            path: "/buttonConfig",
            name: "buttonConfig",
            component: () =>
              import("../views/systemManage/buttonConfig/buttonConfig.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/buttonConfig", // 默认跳转路径
            },
          },
          {
            path: "/buttonManage",
            name: "buttonManage",
            component: () =>
              import("../views/systemManage/button/buttonManage.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/buttonManage", // 默认跳转路径
            },
          },
          {
            path: "/messagTemplate",
            name: "messagTemplate",
            component: () =>
              import("../views/messageCenter/messagTemplate.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/messagTemplate", // 默认跳转路径
            },
          },
          {
            path: "/messagNotice",
            name: "messagNotice",
            component: () => import("../views/messageCenter/messagNotice.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/messagNotice", // 默认跳转路径
            },
          },
          {
            path: "/personalCenter",
            name: "personalCenter",
            component: () =>
              import("../views/personalCenter/personalCenter.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/personalCenter", // 默认跳转路径
            },
          },
          {
            path: "/journalManage",
            name: "journalManage",
            component: () => import("../views/journalManage/journalManage.vue"),
            meta: {
              requireAuth: true, // 是否需要登录验证
              index: "/journalManage", // 默认跳转路径
            },
          },
        ],
      },
    ],
  },
];

// 路由自动化注册（默认注册到index的children里面）(静态路由优先级高于动态自动路由)
const requireComponent = import.meta.glob("../views/**/*.vue"); // 找到 views 路径下的所有 .vue 文件
const indexPathWhiteList = [
  "/",
  "/login",
  "/login",
  "/loginsimple",
  "/lyterminal",
];
// 根路由文件白名单，这些路径不会被自动注册
const indexVuePathWhiteList = [
  "../views/login.vue",
  "../views/lyterminal.vue",
  "../views/loginsimple.vue",
  "../views/index.vue",
  "../views/error/404.vue",
];
// 动态路由数组，用于存储自动注册的子路由
const childrenRouterList = [];

// 遍历所有找到的 .vue 文件
Object.keys(requireComponent).forEach((key) => {
  // 获取组件的名称
  const name = requireComponent[key].name;
  // 排除特定路径的组件
  if (
    name.indexOf("/components/") == -1 &&
    indexVuePathWhiteList.indexOf(name) == -1
  ) {
    let isSame = false;
    const componentName = name.split("/").pop()?.split(".")[0]; // 根据路径截取组件名称（去除后缀和前面目录）
    const path = "/" + componentName;
    // 检查是否已存在相同的路由
    for (var i = 0; i < routes.length; i++) {
      if (indexPathWhiteList.indexOf(routes[i].path) > -1) {
        continue;
      }
      if (routes[i].name === componentName) {
        isSame = true;
        break;
      }
      if (routes[i].path === "/index" && routes[i].children.length > 0) {
        for (var s = 0; s < routes[i].children.length; s++) {
          if (routes[i].children[s].name === componentName) {
            isSame = true;
            break;
          }
        }
      }
    }
    // 如果不存在相同的路由，则添加到动态路由数组中
    if (!isSame) {
      childrenRouterList.push({
        path: path,
        name: componentName,
        component: requireComponent[key],
        meta: {
          requireAuth: true, // 设置需要登录权限
          index: path,
        },
      });
    }
  }
});

// 将动态路由添加到 /index 路由的子路由中
for (let t = 0; t < routes.length; t++) {
  if (routes[t].path == "/index") {
    childrenRouterList.forEach((drouter) => {
      routes[t].children.push(drouter);
    });
    break;
  }
}

// 创建 Vue Router 实例
const router = createRouter({
  // 使用 hash 模式
  history: createWebHashHistory(),
  routes: routes,
});

// 判断访问路径路由 name 是否存在
function isRouterNameExist(name) {
  let isExist = false;
  if (name) {
    if (routes.some((item) => name == item.name)) {
      return true;
    }
    for (let t = 0; t < routes.length; t++) {
      if (routes[t].children && routes[t].children.length > 0) {
        if (routes[t].children.some((item) => name == item.name)) {
          isExist = true;
          break;
        }
      }
    }
  } else {
    return false;
  }
  return isExist;
}

// 判断访问路径路由 path 是否存在
function isRouterPathExist(path) {
  let isExist = false;
  if (path) {
    if (routes.some((item) => path == item.path)) {
      return true;
    }
    for (let t = 0; t < routes.length; t++) {
      if (routes[t].children && routes[t].children.length > 0) {
        if (routes[t].children.some((item) => path == item.path)) {
          isExist = true;
          break;
        }
      }
    }
  } else {
    return false;
  }
  return isExist;
}

/**
 * 路由拦截
 * 权限验证
 */
router.beforeEach((to, from, next) => {
  const store = useMutitabsStore(); // 获取 Vuex store
  // 白名单，这些路由不需要登录权限
  const whiteList = [
    "buttonConfig",
    "menuManage",
    "lyterminal",
    "buttonManage",
  ];
  // 进度条开始
  NProgress.start();
  let userId = store.userId ? store.userId : ""; // 获取用户 ID

  if (to.meta.requireAuth) {
    // 判断该路由是否需要登录权限
    if (userId) {
      // 用户已登录
      let menuList = JSON.parse(getStorage("menuList")); // 获取用户菜单列表
      if (
        menuList &&
        (menuList.filter((item) => item.url == to.name).length > 0 ||
          whiteList.indexOf(to.name) !== -1)
      ) {
        if (to.path) {
          next(); // 允许访问
        } else if (isRouterPathExist(to.path)) {
          next(); // 允许访问
        } else {
          next({ path: "/404" }); // 路由不存在，跳转到 404 页面
        }
      } else {
        next({ path: "/404" }); // 无权限访问，跳转到 404 页面
      }
    } else {
      store.logout("false"); // 用户未登录，注销并跳转到登录页面
      next({ path: "/login" });
    }
  } else {
    if (to.path == "/login" || to.path == "/") {
      // 访问登录或首页
      if (userId) {
        // 用户已登录
        let tabsValue = getStorage("TabsValue"); // 获取当前激活的标签页
        if (tabsValue) {
          if (isRouterNameExist(tabsValue)) {
            // 检查标签页是否存在
            if (tabsValue === "login") {
              next({ path: "/404" }); // 登录页已登录，跳转到 404 页面
            } else {
              store.switchtab(tabsValue); // 切换到指定标签页
            }
          } else {
            next({ path: "/404" }); // 标签页不存在，跳转到 404 页面
          }
        } else {
          let tabsPage = JSON.parse(getStorage("tabsPage")); // 获取所有标签页
          if (tabsPage) {
            if (isRouterNameExist(tabsPage[0].name)) {
              // 检查第一个标签页是否存在
              store.switchtab(tabsPage[0].name); // 切换到第一个标签页
            } else {
              next({ path: "/404" }); // 第一个标签页不存在，跳转到 404 页面
            }
          } else {
            next({ path: "/404" }); // 无标签页，跳转到 404 页面
          }
        }
      } else {
        if (to.name) {
          next(); // 允许访问
        } else if (isRouterPathExist(to.path)) {
          next(); // 允许访问
        } else {
          next({ path: "/404" }); // 路由不存在，跳转到 404 页面
        }
      }
    } else {
      if (to.name) {
        next(); // 允许访问
      } else if (isRouterPathExist(to.path)) {
        next(); // 允许访问
      } else {
        next({ path: "/404" }); // 路由不存在，跳转到 404 页面
      }
    }
  }
});

// 在路由跳转后用 NProgress.done() 标记结束
router.afterEach(() => {
  NProgress.done();
});

export default router;
