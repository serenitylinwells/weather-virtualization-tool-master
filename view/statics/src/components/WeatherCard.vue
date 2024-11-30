<template>
    <div class="forecast-container">
        <div class="forecast-title">7日天气预报</div>
        <div class="divider"></div>
        <div class="forecast-row-wrapper" v-for="(day, index) in dailyForecast" :key="index">
            <div class="forecast-row">
                <!-- 日期 -->
                <span class="day">{{ getDayLabel(day.fxDate, index) }}</span>

                <!-- 天气图标 -->
                <span class="icon">
                    <i :class="getWeatherIconClass(day.iconDay)"></i>
                </span>

                <!-- 最低温 -->
                <span class="temp-min">{{ day.tempMin }}°</span>

                <!-- 温度范围条 -->
                <div class="temp-bar">
                    <!-- 整体背景渐变 -->
                    <div class="temp-background"></div>
                    <!-- 左侧灰色蒙版 -->
                    <div class="temp-mask-left" :style="{ width: `${getPosition(day.tempMin)}%` }"></div>
                    <!-- 右侧灰色蒙版 -->
                    <div class="temp-mask-right" :style="{ width: `${100 - getPosition(day.tempMax)}%` }"></div>
                    <!-- 温度竖线 -->
                    <div v-if="index === 0" class="temp-line" :style="{ left: `${getPosition(temperature)}%` }"></div>
                </div>

                <!-- 最高温 -->
                <span class="temp-max">{{ day.tempMax }}°</span>
            </div>
            <!-- 分割线 -->
            <div v-if="index < dailyForecast.length - 1" class="divider"></div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        dailyForecast: {
            type: Array,
            required: true,
        },
        temperature: {
            type: Number,
            required: false, // 当前温度，仅用于 "今日"
            default: 0,
        },
    },
    data() {
        return {
            minTemp: -20, 
            maxTemp: 30, 
        };
    },
    mounted() {
        this.calculateTempRange(); // 初始化时计算温度范围
    },
    watch: {
        dailyForecast: {
            handler: "calculateTempRange",
            immediate: true,
        },
    },
    methods: {
        // 计算七天内的最高和最低温度
        calculateTempRange() {
            if (this.dailyForecast && this.dailyForecast.length > 0) {
                const temps = this.dailyForecast.flatMap(day => [
                    Number(day.tempMin),
                    Number(day.tempMax),
                ]);
                this.minTemp = Math.min(...temps);
                this.maxTemp = Math.max(...temps);
            }
        },
        // 获取日期标签，返回周几
        getDayLabel(fxDate, index) {
            const daysOfWeek = [
                "周日",
                "周一",
                "周二",
                "周三",
                "周四",
                "周五",
                "周六",
            ];
            if (!fxDate) {
                console.error("日期为空");
                return "未知";
            }
            try {
                const date = new Date(fxDate);
                if (isNaN(date.getTime())) {
                    console.error("无效的日期格式：", fxDate);
                    return "未知";
                }
                if (index === 0) return "今天";
                return daysOfWeek[date.getDay()];
            } catch (error) {
                console.error("解析日期失败：", error);
                return "未知";
            }
        },
        // 获取天气图标的类名
        getWeatherIconClass(iconCode) {
            return `qi-${iconCode}`;
        },
        // 动态计算温度条位置
        getPosition(temp) {
            return ((temp - this.minTemp) / (this.maxTemp - this.minTemp)) * 100;
        },
    },
};
</script>

<style scoped>
.forecast-container {
    position: relative;
    width: 512px;
    height: auto;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    color: white;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.forecast-title {
    font-size: 14px;
    color: rgba(255, 255, 255, 0.6);
    text-align: center;
    margin-bottom: 10px;
}

.forecast-row-wrapper {
    display: flex;
    flex-direction: column;
}

.forecast-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 14px;
    color: #fff;
}

.divider {
    height: 1px;
    background-color: rgba(255, 255, 255, 0.2);
    margin: 10px 0;
}

.day {
    flex: 1;
    text-align: left;
    font-size: 16px;
}

.icon i {
    font-size: 28px;
    color: white;
    margin: 0 10px;
}

.temp-min {
    flex: 0.5;
    text-align: center;
}

.temp-bar {
    flex: 3;
    position: relative;
    height: 10px;
    border-radius: 3px;
    margin: 0 10px;
    overflow: hidden;
}

.temp-background {
    position: absolute;
    width: 100%;
    height: 100%;
    background: linear-gradient(to right,
            #6fc4fd,
            #abd8fd,
            #f8e19d,
            #fcd7a0,
            #f79070);
    z-index: 1;
}

.temp-mask-left {
    position: absolute;
    height: 100%;
    background: rgba(68, 68, 68, 0.8);
    left: 0;
    z-index: 2;
}

.temp-mask-right {
    position: absolute;
    height: 100%;
    background: rgba(68, 68, 68, 0.8);
    right: 0;
    z-index: 2;
}

.temp-line {
    position: absolute;
    height: 100%;
    width: 3px;
    background-color: rgb(255, 255, 255);
    z-index: 3;
}
</style>
