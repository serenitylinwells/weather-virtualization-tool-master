import { createRouter, createWebHistory } from "vue-router";
import WeatherView from "../views/WeatherView.vue"; // 天气主页面

const routes = [
  {
    path: "/",
    name: "Home",
    component: WeatherView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
