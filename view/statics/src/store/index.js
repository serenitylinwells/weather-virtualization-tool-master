import axios from "axios";
import { createStore } from "vuex";

export default createStore({
  state: {
    weatherData: {
      now: {}, // 当前天气数据
      dailyForecast: [], // 7 天预报数据
    },
    selectedCity: {
      name: "",
      id: "",
      lat: "",
      lon: "",
      adm2: "",
      adm1: "",
      country: "",
      tz: "",
      utcOffset: "",
      isDst: "",
      type: "",
      rank: "",
    }, // 存放选中城市的详细信息
  },
  mutations: {
    setWeatherData(state, weatherData) {
      state.weatherData = weatherData; // 更新天气数据
    },
    setSelectedCity(state, city) {
      state.selectedCity = {
        name: city.name || "",
        id: city.id || "",
        lat: city.lat || "",
        lon: city.lon || "",
        adm2: city.adm2 || "",
        adm1: city.adm1 || "",
        country: city.country || "",
        tz: city.tz || "",
        utcOffset: city.utcOffset || "",
        isDst: city.isDst || "0",
        type: city.type || "",
        rank: city.rank || "",
      }; // 提取并存储城市详细信息
    },
  },
  actions: {
    async fetchWeatherData({ commit }, location) {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8081/weatherTool/weather-api/getWeather/${location}`
        );

        const data = response.data.data; // 获取后端返回的数据

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

        commit("setWeatherData", weatherData); // 更新天气数据
      } catch (error) {
        console.error("获取天气数据失败：", error);
      }
    },
    async fetchCityData({ commit }, location) {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8081/weatherTool/weather-api/getCity/${location}`
        );
        if (response.data.code === 0) {
          const city = response.data.data.location[0]; // 假设选取第一个匹配的城市
          commit("setSelectedCity", city); // 更新选中的城市数据
        }
      } catch (error) {
        console.error("获取城市数据失败：", error);
      }
    },
  },
  getters: {
    weatherData: (state) => state.weatherData, // 返回天气数据
    selectedCity: (state) => state.selectedCity, // 返回选中的城市详细信息
  },
});
