import { createRouter, createWebHistory } from "vue-router";
import WeatherView from "../views/WeatherView.vue"; // 天气主页面
import SettingView from "../views/SettingView.vue"; // 设置页面
import LoginView from "../views/LoginView.vue"; // 登录页面

const routes = [
  {
    path: "/",
    name: "Home",
    component: WeatherView
  },
  {
    path: "/setting",
    name: "Setting",
    component: SettingView
  },
  {
    path: "/login",
    name: "Login",
    component: LoginView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
