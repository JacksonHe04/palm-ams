// @/router/index.js 路由管理文件
// createRouter：创建router实例对象
// createWebHistory：创建history模式的路由
import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/Login/index.vue'
import Layout from '@/views/Layout/index.vue'
import Home from '@/views/Home/index.vue'
import Admin from '@/views/Admin/index.vue'
import Apply from '@/views/Apply/index.vue'
import About from '@/views/About/index.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    // path和component对应关系的位置
    routes: [
        {
            path: '/',
            component: Layout,
            children: [
                {
                    path: '',
                    component: Home,
                    meta: { title: '欢迎来到PALM实验室' }
                },
                {
                    path: '/apply',
                    component: Apply,
                    meta: { title: '申请PALM实验室' }
                },
                {
                    path: '/login',
                    component: Login,
                    meta: { title: '登录PALM实验室' }
                },
                {
                    path: '/admin',
                    component: Admin,
                    meta: { title: 'PALM实验室后台管理' }
                },
                {
                    path: '/about',
                    component: About,
                    meta: { title: '关于开发者' }
                },

            ]
        },

    ],
    // 路由滚动行为定制
    scrollBehavior () {
        return {
            top: 0
        }
    }
})

// 全局前置守卫
router.beforeEach((to, from, next) => {
    document.title = to.meta.title || 'palm';
    next();
});

export default router
