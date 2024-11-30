<template>
    <div class="temperature-card">
        <!-- 左侧文字部分 -->
        <div class="text-section">
            <p class="title">体感温度</p>
            <h3 class="value">{{ feelsLike }}°</h3>
            <p class="comment">{{ comment }}</p>
        </div>
        <!-- 右侧温度计部分 -->
        <div class="temperature-bar">
            <div class="temperature-indicator" :style="{ bottom: `${getPosition(feelsLike)}%` }"></div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        feelsLike: {
            type: Number,
            default: 20,
        },
    },
    computed: {
        comment() {
            if (this.feelsLike < 10) return "感觉很冷";
            if (this.feelsLike > 30) return "感觉很热";
            return "温度适中";
        }
    },
    methods: {
        getPosition(temp) {
            // 将体感温度从 -10 到 50 映射到 0% 到 100%
            const minTemp = -10;
            const maxTemp = 50;
            return ((temp - minTemp) / (maxTemp - minTemp)) * 100; // 转换为百分比
        }
    }
};
</script>

<style scoped>
.temperature-card {
    display: flex;
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

/* 左侧文字部分 */
.text-section {
    flex: 1;
    text-align: left;
    padding-left: 40px;
    padding-right: 10px;
}

.title {
    font-size: 14px;
    color: #ccc;
    margin: 0;
}

.value {
    font-size: 36px;
    color: white;
    font-weight: bold;
    margin: 5px 0;
}

.comment {
    font-size: 12px;
    color: #ccc;
    margin: 0;
}

/* 右侧温度计部分 */
.temperature-bar {
    position: relative;
    width: 20px;
    margin-right: 30px;
    height: 80%;
    background: linear-gradient(to top, 
    #6fc4fd, /* 淡蓝 */
    #abd8fd, /* 浅天蓝 */
    #f8e19d, /* 浅黄色 */
    #fcd7a0, /* 淡橙色 */
    #f79070 /* 浅粉橙 */
);
    border-radius: 10px;
    overflow: hidden;
}

/* 温度指示器 */
.temperature-indicator {
    position: absolute;
    left: 0;
    right: 0;
    height: 5px;
    background: white;
    border-radius: 3px;
    box-shadow: 0 0 3px rgba(0, 0, 0, 0.5);
    transition: bottom 0.3s ease;
}
</style>