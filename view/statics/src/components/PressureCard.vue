<template>
    <div class="card">
        <p class="title">气压</p>
        <h3 class="value">{{ pressure }} 百帕</h3>
    </div>
</template>

<script>
export default {
    props: ["pressure"]
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
</style>