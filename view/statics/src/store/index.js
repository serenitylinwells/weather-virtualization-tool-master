import axios from "axios";
import { createStore } from "vuex";

export default createStore({
  state: {
    weatherData: {
      now: {}, // 初始化当前天气数据为空对象
      dailyForecast: [], // 初始化 7 天数据为空数组
    },
  },
  mutations: {
    setWeatherData(state, weatherData) {
      state.weatherData = weatherData; // 更新天气数据
    },
  },
  actions: {
    async fetchWeatherData({ commit }, locationId) {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8081/weatherTool/weather-api/getWeather/${locationId}`
        );

        const data = response.data.data; // 获取后端返回的数据

        // 提取每日数据
        const dailyForecast = data.daily.map((day) => ({
          fxDate: day.fxDate, // 日期
          tempMax: day.tempMax, // 最高温
          tempMin: day.tempMin, // 最低温
          iconDay: day.iconDay, // 白天图标
          textDay: day.textDay, // 白天天气描述
          iconNight: day.iconNight, // 夜晚图标
          textNight: day.textNight, // 夜晚天气描述
          moonrise: day.moonrise,
          moonset: day.moonset,
          moonPhase: day.moonPhase,
          moonPhaseIcon: day.moonPhaseIcon,
        }));

        // 构造完整的 weatherData 数据结构
        const weatherData = {
          now: {
            temp: data.now.temp,
            feelsLike: data.now.feelsLike,
            text: data.now.text,
            windScale: data.now.windScale,
            windSpeed: data.now.windSpeed,
            windDir: data.now.windDir,
            wind360: data.now.wind360,
            pressure: data.now.pressure,
            humidity: data.now.humidity,
            precip: data.now.precip,
            visibility: data.now.vis,
            obsTime: data.now.obsTime,
          },
          sunrise: data.daily[0]?.sunrise, // 日出时间
          sunset: data.daily[0]?.sunset, // 日落时间
          dailyForecast, // 7 天预报
        };

        commit("setWeatherData", weatherData); // 更新 Vuex 状态
      } catch (error) {
        console.error("获取天气数据失败：", error);
      }
    },
  },
  getters: {
    weatherData: (state) => state.weatherData, // 返回天气数据
  },
});
