// createRouter：创建router实例对象
// createWebHistory：创建history模式的路由

import { createRouter, createWebHistory } from 'vue-router'
// import Login from '@/views/Login/index.vue'
import Layout from '../components/Hello.vue'
import Home from '../components/Home.vue'
// import MedicalDatabase from '@/views/MedicalDataBase/index.vue'
// import NLP from '@/views/NLP/index.vue'
// import SubCategory from '@/views/SubCategory/index.vue'
// import Detail from '@/views/Detail/index.vue'
// import CartList from '@/views/CartList/index.vue'
// import Checkout from '@/views/Checkout/index.vue'
// import Pay from '@/views/Pay/index.vue'
// import PayBack from '@/views/Pay/PayBack.vue'
// import Member from '@/views/Member/index.vue'
// import UserInfo from '@/views/Member/components/UserInfo.vue'
// import UserOrder from '@/views/Member/components/UserOrder.vue'

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
                    meta: { title: '首页' }
                },
                // {
                //     path: 'MedicalDatabase',
                //     component: MedicalDatabase,
                //     meta: { title: '医疗数据库' }
                // },
                // {
                //     path: 'nlp',
                //     component: NLP,
                //     meta: { title: 'NLP算法处理' }
                // },
                // {
                //     path: 'login',
                //     component: Login,
                //     meta: { title: '登录超级医生' }
                // }
                //         {
                //             path: 'category/sub/:id',
                //             component: SubCategory,
                //             meta: { title: '子分类' }
                //         },
                //         {
                //             path: 'detail/:id',
                //             component: Detail,
                //             meta: { title: '图书详情' }
                //         },
                //         {
                //             path: 'cartlist',
                //             component: CartList,
                //             meta: { title: '购物车' }
                //         },
                //         {
                //             path: 'checkout',
                //             component: Checkout,
                //             meta: { title: '图书结算' }
                //         },
                //         {
                //             path: 'pay',
                //             component: Pay,
                //             meta: { title: '支付页' }
                //         },
                //         {
                //             path: 'paycallback',
                //             component: PayBack,
                //             meta: { title: '支付返回' }
                //         },
                //         {
                //             path: 'member',
                //             component: Member,
                //             children: [
                //                 {
                //                     path: '',
                //                     component: UserInfo,
                //                     meta: { title: '用户信息' }
                //                 },
                //                 {
                //                     path: 'order',
                //                     component: UserOrder,
                //                     meta: { title: '订单列表' }
                //                 }
                //             ]
                //         }
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
