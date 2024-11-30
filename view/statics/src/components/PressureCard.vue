<template>
    <div class="circle-container">
        <div class="circle">
            <div v-for="i in 72" :key="i" class="gauge-tick" :style="getTickStyle(i)"></div>
            <div class="pressure-indicator" :style="getPressureLineStyle"></div>
            <div class="pressure-value">{{ pressure }} 百帕</div>
            <div class="low">Low</div>
            <div class="high">High</div>
            <div class="title">气压</div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        pressure: {
            type: Number,
            default: 1000,
        },
    },
    computed: {
        // 计算当前气压线的位置
        getPressureLineStyle() {
            const angle = 170 + (this.pressure - 900) / 5 * 5;
            return {
                transform: `rotate(${angle}deg)`,  // 控制气压线的位置
                transformOrigin: '0 50%',
                top: '50%',
                left: '50%',
                position: 'absolute',
            };
        }
    },
    methods: {
        // 计算每个刻度线的旋转角度
        getTickStyle(index) {
            const angle = index * 5;
            const transform = `rotate(${angle}deg)`;
            return {
                transform,
                transformOrigin: '0%, 50%',
            };
        }
    }
};
</script>

<style scoped>
.circle-container {
    width: 226px;
    height: 226px;
    position: relative;
    text-align: center;
}

.circle {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    position: relative;
    clip-path: inset(0 0 25% 0);
}

.gauge-tick {
    position: absolute;
    width: 96px;
    height: 2px;
    background-color: #fff;
    top: 50%;
    left: 50%;
    transform-origin: 0 50%;
    clip-path: inset(0 0 0 90%);
}

.pressure-indicator {
    position: absolute;
    width: 100px;
    height: 4px;
    background-color: #ffffff;
    top: 50%;
    left: 50%;
    transform-origin: 0 50%;
    z-index: 2;
    clip-path: inset(0 0 0 82%);
}

.pressure-value {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #fff;
    font-size: 18px;
    font-weight: bold;
    z-index: 3;
}

.low,
.high {
    position: absolute;
    font-size: 16px;
    right: 45%;
    top: 67%;
    left: 45%;
    color: white;
    font-weight: bold;
    z-index: 4;
}

.low {
    bottom: 15px;
    left: 10px;
}

.high {
    bottom: 15px;
    right: 10px;
}

.title {
    position: absolute;
    font-size: 14px;
    right: 45%;
    top: 25%;
    color: #ccc;
    font-weight: bold;
    z-index: 4;
}
</style>
