<template>
  <div class="weather-view">
    <div class="background"></div>
    <div class="weather-container">
      <LocationDisplay :location="weatherData.location" :temperature="weatherData.now.temp"
        :weatherText="weatherData.now.text" />
      <div>
        <WeatherCard :dailyForecast="weatherData.dailyForecast" :temperature="weatherData.now.temp" />
      </div>
      <div>
        <WindCard :windScale="weatherData.now.windScale" :windSpeed="weatherData.now.windSpeed"
          :windDir="weatherData.now.windDir" :wind360="weatherData.now.wind360" class="double-width-card" />
      </div>
      <div class="cards">
        <TemperatureCard :feelsLike="weatherData.now.feelsLike" />
        <MoonPhaseCard :dailyForecast="weatherData.dailyForecast" />
        <SunsetCard :sunrise="weatherData.sunrise" :sunset="weatherData.sunset" :obsTime="weatherData.now.obsTime" />
        <RainfallCard :precip="weatherData.now.precip" />
        <VisibilityCard :visibility="weatherData.now.visibility" />
        <PressureCard :pressure="weatherData.now.pressure" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import LocationDisplay from "../components/LocationDisplay.vue";
import TemperatureCard from "../components/TemperatureCard.vue";
import SunsetCard from "../components/SunsetCard.vue";
import RainfallCard from "../components/RainfallCard.vue";
import VisibilityCard from "../components/VisibilityCard.vue";
import PressureCard from "../components/PressureCard.vue";
import WindCard from "../components/WindCard.vue";
import WeatherCard from "../components/WeatherCard.vue";
import MoonPhaseCard from "../components/MoonPhaseCard.vue";
import axios from "axios";

export default {
  components: {
    LocationDisplay,
    TemperatureCard,
    SunsetCard,
    RainfallCard,
    VisibilityCard,
    PressureCard,
    WindCard,
    WeatherCard,
    MoonPhaseCard
  },
  computed: {
    ...mapGetters(["weatherData"]),
  },
  mounted() {
    this.getUserLocation();  // 用浏览器 Geolocation API 获取位置
  },
  methods: {
    // 用浏览器 Geolocation API 获取经纬度
    async getUserLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          async (position) => {
            let lat = position.coords.latitude;
            let lon = position.coords.longitude;

            lat = lat.toFixed(2);
            lon = lon.toFixed(2);

            // 使用经纬度查询天气数据
            this.fetchWeatherDataByCoordinates(lat, lon);
          },
          (error) => {
            console.error("Geolocation 获取失败: ", error);
          }
        );
      } else {
        console.error("浏览器不支持 Geolocation API");
      }
    },

    async fetchWeatherDataByCoordinates(lat, lon) {
      try {
        // 通过经纬度获取天气数据
        const response = await axios.get(
          `http://127.0.0.1:8081/weatherTool/weather-api/getWeather/${lon},${lat}`
        );
        const data = response.data.data; // 获取后端返回的数据

        // 提取每日数据
        const dailyForecast = data.daily.map((day) => ({
          fxDate: day.fxDate,
          tempMax: day.tempMax,
          tempMin: day.tempMin,
          iconDay: day.iconDay,
          textDay: day.textDay,
          iconNight: day.iconNight,
          textNight: day.textNight,
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
          sunrise: data.daily[0]?.sunrise,
          sunset: data.daily[0]?.sunset,
          dailyForecast,
        };

        this.$store.commit("setWeatherData", weatherData); // 更新 Vuex 状态
      } catch (error) {
        console.error("获取天气数据失败：", error);
      }
    },
  },
};
</script>

<style scoped>
.weather-view {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgb(52, 66, 66);
  background-size: cover;
  z-index: -1;
}

.weather-container {
  position: relative;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  height: 100vh;
  overflow-y: scroll;
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: center;
}

.weather-container::-webkit-scrollbar {
  display: none;
}

.weather-container {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  /* 默认两列布局 */
  gap: 20px;
  width: calc(100% - 40px);
  max-width: 1200px;
  margin: 0 auto;
}

@media (max-width: 768px) {
  .cards {
    grid-template-columns: 1fr;
  }
}


.cards>* {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(15px);
  border-radius: 15px;
  padding: 20px;
  aspect-ratio: 1 / 1;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
}
</style>
