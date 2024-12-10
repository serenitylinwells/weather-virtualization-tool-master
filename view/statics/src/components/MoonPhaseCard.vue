<template>
    <div class="moon-phase-card">
        <!-- 月相图标 -->
        <div class="moon-icon">
            <i :class="getMoonPhaseIcon(currentMoonPhaseIcon)"></i>
        </div>
        <div class="title">月相</div>
        <!-- 月相描述 -->
        <div class="moon-description">
            <p class="moon-phase">{{ currentMoonPhase }}</p>
            <p class="moon-times">
                月出: {{ currentMoonrise }} | 月落: {{ currentMoonset }}
            </p>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        dailyForecast: {
            type: Array, // 指定 prop 类型为数组
            default: () => [], // 默认值为空数组
        },
    },
    computed: {
        // 获取当天的每日天气数据
        currentDayForecast() {
            return this.dailyForecast[0] || {
                moonPhase: "未知月相",
                moonPhaseIcon: "800", // 默认月相图标
                moonrise: "未知",
                moonset: "未知",
            };
        },
        // 获取当天月相描述
        currentMoonPhase() {
            return this.currentDayForecast.moonPhase;
        },
        // 获取当天月相图标代码
        currentMoonPhaseIcon() {
            return this.currentDayForecast.moonPhaseIcon;
        },
        // 获取当天月出时间
        currentMoonrise() {
            return this.currentDayForecast.moonrise;
        },
        // 获取当天月落时间
        currentMoonset() {
            return this.currentDayForecast.moonset;
        },
    },
    methods: {
        // 获取月相图标的类名
        getMoonPhaseIcon(iconCode) {
            return `qi-${iconCode}`;
        },
    },
};
</script>

<style scoped>
.moon-phase-card {
    justify-content: space-between;
    align-items: center;
    width: 100%;
    max-width: 226px;
    height: 100%;
    max-height: 226px;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
}

.title {
    position: absolute;
    font-size: 14px;
    right: 45%;
    top: 54%;
    color: #ccc;
    font-weight: bold;
    z-index: 4;
}

.moon-icon i {
    font-size: 80px;
    color: white;
}

.moon-icon {
    margin-top: 20px;
}

.moon-description {
    padding-top: 25px;
    font-size: 16px;
    color: white;
}

.moon-phase {
    font-weight: bold;
    font-size: 18px;
}

.moon-times {
    font-size: 14px;
    color: #ccc;
}
</style>
