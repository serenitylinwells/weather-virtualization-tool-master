<template>
  <div class="card">
    <h2 class="location">{{ location }}</h2>
    <p class="adm1">行政区: {{ adm1 }}</p>
    <p class="rank">评分: {{ rank }}</p>
    <p class="temperature">{{ temperature }}° | {{ weatherText }}</p>
  </div>
</template>

<script>
export default {
  props: {
    location: {
      default: "你的位置",
    },
    adm1: {
      default: "未知区域",
    },
    rank: {
      default: "未知",
    },
    temperature: {
      default: "22",
    },
    weatherText: {
      default: "舒适",
    },
  },
};
</script>

<style scoped>
.card {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  border-radius: 15px;
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  aspect-ratio: 2.2 / 1;
}

.location {
  font-size: 24px;
  color: white;
}

.adm1,
.rank {
  font-size: 14px;
  color: #ccc;
}

.temperature {
  font-size: 14px;
  color: #ccc;
}
</style>
