<template>
  <div class="weather-view">
    <div class="background"></div>
    <div class="weather-container">
      <LocationDisplay
        :location="weatherData.location"
        :temperature="weatherData.temp"
        :weatherText="weatherData.text"
      />
      <div class="cards">
        <TemperatureCard :feltTemp="weatherData.feltTemp" />
        <WindCard
          :windScale="weatherData.windScale"
          :windSpeed="weatherData.windSpeed"
          :windDir="weatherData.windDir"
        />
        <SunsetCard
          :sunrise="weatherData.sunrise"
          :sunset="weatherData.sunset"
        />
        <RainfallCard :precip="weatherData.precip" />
        <VisibilityCard :visibility="weatherData.visibility" />
        <PressureCard :pressure="weatherData.pressure" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import LocationDisplay from "../components/LocationDisplay.vue";
import TemperatureCard from "../components/TemperatureCard.vue";
import WindCard from "../components/WindCard.vue";
import SunsetCard from "../components/SunsetCard.vue";
import RainfallCard from "../components/RainfallCard.vue";
import VisibilityCard from "../components/VisibilityCard.vue";
import PressureCard from "../components/PressureCard.vue";

export default {
  components: {
    LocationDisplay,
    TemperatureCard,
    WindCard,
    SunsetCard,
    RainfallCard,
    VisibilityCard,
    PressureCard,
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
}

.background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url('/public/pexels-veeterzy-39811.jpg') no-repeat center center fixed;
  background-size: cover;
  z-index: -1;
}

.weather-container {
  position: relative;
  width: 100%;
  max-width: 1200px; /* 限制最大宽度 */
  margin: 0 auto;
  padding: 20px;
  overflow-y: auto; /* 启用滚动 */
  height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: center; /* 水平居中 */
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
  grid-template-columns: repeat(2, 1fr); /* 两列布局 */
  gap: 20px;
  width: calc(100% - 40px); /* 确保屏幕宽度，并留出间距 */
  max-width: 1200px;
  margin: 0 auto;
}

.cards > * {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  border-radius: 15px;
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  aspect-ratio: 1 / 1; /* 保持正方形比例 */
}
</style>
