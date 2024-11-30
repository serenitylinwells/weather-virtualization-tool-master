<template>
  <div class="weather-view">
    <div class="background"></div>
    <div class="weather-container">
      <!-- 位置和当前天气信息 -->
      <LocationDisplay 
        :location="weatherData.location" 
        :temperature="weatherData.now.temp" 
        :weatherText="weatherData.now.text" 
      />

      <!-- 天气预报卡片 -->
      <div>
        <WeatherCard :dailyForecast="weatherData.dailyForecast" :temperature="weatherData.now.temp" />
      </div>
      <!-- 风速风向信息 -->
      <div>
        <WindCard
          :windScale="weatherData.now.windScale" 
          :windSpeed="weatherData.now.windSpeed" 
          :windDir="weatherData.now.windDir" 
          :wind360="weatherData.now.wind360" 
          class="double-width-card" 
        />
      </div>

      <!-- 其他信息卡片 -->
      <div class="cards">
        <TemperatureCard :feelsLike="weatherData.now.feelsLike" />
        <MoonPhaseCard :dailyForecast="weatherData.dailyForecast"/>
        <SunsetCard 
          :sunrise="weatherData.sunrise" 
          :sunset="weatherData.sunset" 
          :obsTime="weatherData.now.obsTime" 
        />
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
    // 模拟 LocationID，后续可以从实际输入或地理位置获取
    const locationId = "101280601"; // 示例：龙岗区的 LocationID
    this.$store.dispatch("fetchWeatherData", locationId);
  },
};
</script>

<style scoped>
.weather-view {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  /* 确保背景不滚动 */
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

/* 隐藏滚动条 */
.weather-container::-webkit-scrollbar {
  display: none;
}

.weather-container {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

/* 使用Grid布局并支持响应式 */
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
    /* 小屏幕设备上每行1个卡片 */
  }
}


.cards>* {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(15px);
  /* 背景模糊 */
  border-radius: 15px;
  padding: 20px;
  aspect-ratio: 1 / 1;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  /* 保持正方形比例 */
}
</style>
