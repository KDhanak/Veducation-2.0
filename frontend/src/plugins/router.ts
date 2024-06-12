import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

const routes: Array<RouteRecordRaw> = [
    {
        path: "/home",
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

export default router;
