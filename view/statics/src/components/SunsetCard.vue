<template>
    <div class ="Sunsetcard">
        <div>
            <canvas ref="sunCanvas" width="200" height="200"></canvas>
        </div>
        <div class="title">日出</div>
    </div>
</template>

<script>
export default {
    props: {
        obsTime: {  // 观测时间
            type: String,
            default: '2024-11-28T11:50+08:00'
        },
        sunrise: {  // 日出时间
            type: String,
            default: '06:00'
        },
        sunset: {  // 日落时间
            type: String,
            default: '19:00'
        }
    },
    data() {
        return {
            currentObsTime: this.obsTime,  // 初始时用传递的值或默认值
        };
    },
    mounted() {
        this.drawSunCircle();
    },
    watch: {
        // 监听 obsTime 的变化，一旦更新，更新 currentObsTime 并重新绘制
        obsTime(newVal) {
            console.log("Observed time updated:", newVal);
            this.currentObsTime = newVal;
            this.drawSunCircle();  
        }
    },
    methods: {
        // 解析时间并转换为分钟
        parseTime(timeStr) {
            if (!timeStr || !timeStr.includes(":")) {
                console.error("Invalid time format:", timeStr);
                return 0; 
            }

            const match = timeStr.match(/^(\d{1,2}):(\d{2})$/);
            if (match) {
                const hour = parseInt(match[1], 10);
                const minute = parseInt(match[2], 10);
                return hour * 60 + minute;
            } else {
                console.error("Invalid time format:", timeStr);
                return 0;
            }
        },

        // 解析 obsTime 并提取时间部分
        parseObsTime() {
            // 提取时间部分（去掉日期和时区）
            const timeStr = this.currentObsTime.split('T')[1].split('+')[0];  
            console.log("Parsed time string:", timeStr);  
            return this.parseTime(timeStr);  
        },

        drawSunCircle() {
            const canvas = this.$refs.sunCanvas;
            const ctx = canvas.getContext("2d");

            const centerX = 100;
            const centerY = 100;
            const radius = 80; 

            const sunriseTime = this.parseTime(this.sunrise);
            const sunsetTime = this.parseTime(this.sunset);
            const obsTime = this.parseObsTime(); 

            // 计算角度
            const totalMinutesInDay = 24 * 60;  
            const sunriseAngle = (sunriseTime / totalMinutesInDay) * 2 * Math.PI; 
            const sunsetAngle = (sunsetTime / totalMinutesInDay) * 2 * Math.PI; 
            const obsAngle = (obsTime / totalMinutesInDay) * 2 * Math.PI; 

            // 绘制圆形
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
            ctx.lineWidth = 5;
            ctx.strokeStyle = "#FFFFFF"; 
            ctx.stroke();

            // 绘制6:00和18:00的横线
            const sixX = centerX + Math.cos(Math.PI) * radius;  
            const sixY = centerY + Math.sin(Math.PI) * radius;
            const eighteenX = centerX + Math.cos(0) * radius;  
            const eighteenY = centerY + Math.sin(0) * radius;

            ctx.beginPath();
            ctx.moveTo(sixX - 2, sixY); // 6:00横线
            ctx.lineTo(sixX + 2, sixY);
            ctx.lineWidth = 2;
            ctx.strokeStyle = "#FFFFFF";
            ctx.stroke();

            ctx.beginPath();
            ctx.moveTo(eighteenX - 2, eighteenY); // 18:00横线
            ctx.lineTo(eighteenX + 2, eighteenY);
            ctx.stroke();

            // 绘制日出日落位置（白色）
            const sunSetX = centerX - Math.cos(sunriseAngle - Math.PI / 2) * radius;
            const sunSetY = centerY - Math.sin(sunriseAngle - Math.PI / 2) * radius;
            const sunRiseX = centerX - Math.cos(sunsetAngle - Math.PI / 2) * radius;
            const sunRiseY = centerY - Math.sin(sunsetAngle - Math.PI / 2) * radius;

            // 绘制日出位置横线
            ctx.beginPath();
            ctx.moveTo(sunRiseX - 10, sunRiseY);  
            ctx.lineTo(sunRiseX + 10, sunRiseY);  
            ctx.lineWidth = 2;
            ctx.strokeStyle = "#FFFFFF"; 
            ctx.stroke();

            // 绘制日落位置横线
            ctx.beginPath();
            ctx.moveTo(sunSetX - 10, sunSetY);  
            ctx.lineTo(sunSetX + 10, sunSetY);  
            ctx.stroke();

            // 绘制观测时间位置
            const obsX = centerX - Math.cos(obsAngle - Math.PI / 2) * radius; 
            const obsY = centerY - Math.sin(obsAngle - Math.PI / 2) * radius;

            // 判断白天或夜晚
            const isDaytime = obsTime >= sunriseTime && obsTime <= sunsetTime;

            // 显示观测时间，白天白色，晚上黑色
            ctx.beginPath();
            ctx.arc(obsX, obsY, 6, 0, 2 * Math.PI);  
            ctx.fillStyle = isDaytime ? "#FFFFFF" : "#4B4B4B"; 
            ctx.fill();


            // 在圆形中间显示日出和日落时间
            ctx.font = "13px Arial";
            ctx.fillText(`SUNRISE: ${this.sunrise}`, centerX - 50, centerY - 10);
            ctx.fillText(`SUNSET: ${this.sunset}`, centerX - 46, centerY + 20);

            // 画日出到日落之间的轨道，表示晚上
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius, (sunsetAngle) + Math.PI / 2, (sunriseAngle) + Math.PI / 2, false);
            ctx.lineWidth = 6;
            ctx.strokeStyle = "#4B4B4B"; 
            ctx.stroke();

            ctx.beginPath();
            ctx.arc(obsX, obsY, 6, 0, 2 * Math.PI);  
            ctx.lineWidth = 1; 
            ctx.strokeStyle = "#FFFFFF"; 
            ctx.stroke();
        }
    }
};
</script>
<style scoped>
.title {
    position: absolute;
    font-size: 14px;
    right: 45%;
    top: 25%;
    color: #ccc;
    font-weight: bold;
    z-index: 4;
}

.SunsetCard {
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
</style>
