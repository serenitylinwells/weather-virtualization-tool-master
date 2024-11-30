<template>
    <div class="card">
        <!-- 左侧文字部分 -->
        <div class="details">
            <p>风力: {{ windScale }}级</p>
            <p>风速: {{ windSpeed }} km/h</p>
            <p>方向: {{ windDir }}</p>
            <p>风向: {{ wind360 }}°</p>
        </div>
        <!-- 分割线 -->
        <div class="divider"></div>
        <!-- 右侧圆盘图部分 -->
        <div class="visualization">
            <div class="circle">
                <!-- 方向标签 -->
                <div class="label north">N</div>
                <div class="label east">E</div>
                <div class="label south">S</div>
                <div class="label west">W</div>
                <div class="center-dot"></div>
                <!-- 风向指针 -->
                <div class="indicator" :style="{ transform: `rotate(${wind360}deg)` }"></div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "WindCard",
    props: {
        windScale: {
            type: Number,
            default: 0,
        },
        windSpeed: {
            type: Number,
            default: 0,
        },
        windDir: {
            type: String,
            default: "NE",
        },
        wind360: {
            type: Number,
            default: 60
        },
    },
};
</script>

<style scoped>
.card {
    position: relative;
    width: 512px;
    height: 200px;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    color: white;
}

.details {
    position: absolute;
    top: 45px;
    left: 60px;
    width: 150px;
}

.details p {
    margin: 15px 0;
}

.divider {
    position: absolute;
    top: 20px;
    bottom: 20px;
    left: 275px; 
    width: 1px;
    background: gray;
}

.visualization {
    position: absolute;
    top: 50%;
    left: 350px; 
    transform: translateY(-50%);
    width: 100px;
    height: 120px;
}

.circle {
    position: relative;
    width: 130px;
    height: 130px;
    margin: 0 auto;
    border-radius: 50%;
    border: 3px solid gray;
}

.label {
    position: absolute;
    font-size: 12px;
    font-weight: bold;
    color: white;
}

.north {
    top: -12px;
    left: 50%;
    transform: translateX(-50%);
}

.east {
    right: -12px;
    top: 50%;
    transform: translateY(-50%);
}

.south {
    bottom: -12px;
    left: 50%;
    transform: translateX(-50%);
}

.west {
    left: -12px;
    top: 50%;
    transform: translateY(-50%);
}

.center-dot {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 10px;
    height: 10px;
    background-color: white;
    border-radius: 50%;
    transform: translate(-50%, -50%);
}

.indicator {
    position: absolute;
    width: 3px;
    height: 40px;
    background: white;
    top: 20%;
    left: 50%;
    transform-origin: bottom;
}
</style>