import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Cookies from "js-cookie";

const routes: Array<RouteRecordRaw> = [
    {
        path: "/",
        name: "Home",
        component: () => import("../components/Home.vue"),
    },
    {
        path: "/login",
        name: "Login",
        component: () => import("../components/Login.vue"),
    },
    {
        path: "/register",
        name: "Register",
        component: () => import ("../components/Registration.vue")
    }
];

const router = createRouter({
    routes,
    history: createWebHistory(),
});

router.beforeEach((to, _, next) => {
    const accessToken = Cookies.get("access_token");

    if (to.meta.requiresAuth && !accessToken) {
        next({name: "Login"});
    } else {
        next();
    }
});

export default router;
