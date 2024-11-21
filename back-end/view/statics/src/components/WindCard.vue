<template>
  <div class="card">
    <p class="title">风力</p>
    <h3 class="value">{{ windScale }}级</h3>
    <p class="comment">风速：{{ windSpeed }} 公里/小时</p>
    <p class="comment">风向：{{ windDir }}</p>
  </div>
</template>

<script>
export default {
  props: ["windScale", "windSpeed", "windDir"]
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
  aspect-ratio: 1 / 1;
}

.title {
  font-size: 14px;
  color: #ccc;
}

.value {
  font-size: 36px;
  color: white;
  font-weight: bold;
  margin: 10px 0;
}

.comment {
  font-size: 12px;
  color: #ccc;
}
</style>
