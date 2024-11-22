import axios from "axios";
import { createStore } from "vuex";

export default createStore({
  state: {
    weatherData: {}, // 保存天气数据
    errorMessage: null, // 保存错误信息
  },
  mutations: {
    setWeatherData(state, weatherData) {
      state.weatherData = weatherData;
    },
    setErrorMessage(state, message) {
      state.errorMessage = message;
    },
  },
  actions: {
    async fetchWeatherData({ commit }, locationId) {
      try {
        // 发送 GET 请求到后端
        const response = await axios.get(
          `http://127.0.0.1:8081/weatherTool/weather-api/getWeather/byLocationId/${locationId}`
        );

        // 判断后端返回的状态码
        if (response.data.code === 0) {
          commit("setWeatherData", response.data.data); // 保存数据到 Vuex
        } else {
          console.error("后端返回错误：", response.data.msg);
          commit("setErrorMessage", response.data.msg); // 保存错误信息
        }
      } catch (error) {
        console.error("获取天气数据失败：", error.message);
        commit("setErrorMessage", "请求失败，请检查网络或后端状态"); // 设置通用错误信息
      }
    },
  },
  getters: {
    weatherData: (state) => state.weatherData,
    errorMessage: (state) => state.errorMessage,
  },
});
