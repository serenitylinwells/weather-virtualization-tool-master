<template>
  <div class="card">
    <h2 class="location">{{ location }}</h2>
    <p class="temperature">{{ temperature }}° | {{ weatherText }}</p>
  </div>
</template>

<script>
export default {
  props: {
        location: { 
            default: '深圳'
        },
        temperature: { 
            default: '22'
        },
        weatherText: { 
            default: '舒适'
        }
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
  aspect-ratio: 4 / 1;
}

.location {
  font-size: 24px;
  color: white;
}

.temperature {
  font-size: 14px;
  color: #ccc;
  margin-top: 10px;
}
</style>
