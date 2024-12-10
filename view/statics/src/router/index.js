import { createRouter, createWebHistory } from "vue-router";
import WeatherView from "../views/WeatherView.vue"; // 天气主页面
import SettingView from "../views/SettingView.vue"; // 设置页面
import LoginView from "../views/LoginView.vue"; // 登录页面
import SearchWeatherView from "../views/SearchWeatherView.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: WeatherView
  },
  {
    path: "/setting",
    name: "Setting",
    component: SettingView,
    meta: { requiresAuth: true }
  },
  {
    path: "/login",
    name: "Login",
    component: LoginView
  },
  {
    path: "/search-weather",
    name: "SearchWeather",
    component: SearchWeatherView
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;

router.beforeEach((to, from, next) => {
  const isLoggedIn = !!localStorage.getItem("token");
  if (to.meta.requiresAuth && !isLoggedIn) {
    next("/login"); // 未登录时跳转到登录页面
  } else {
    next(); // 放行
  }
});