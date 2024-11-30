<template>
    <div class="card">
        <p class="title">能见度</p>
        <h3 class="value">{{ visibility }} 公里</h3>
        <p class="comment">{{ comment }}</p>
        <div class="visualization">
            <div class="gradient-bar" :style="{ background: getGradient(visibility) }"></div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        visibility: {  // 能见度 (Visibility)
            type: Number,
            default: 20,  // 默认值为20公里
        },
    },
    computed: {
        comment() {
            if (this.visibility > 20) {
                return "视野非常好"; // Very clear visibility
            } else if (this.visibility > 10) {
                return "能见度较好"; // Good visibility
            } else if (this.visibility > 5) {
                return "能见度一般"; // Average visibility
            } else {
                return "能见度较低"; // Poor visibility
            }
        }
    },
    methods: {
        getGradient(visibility) {
            // 将能见度映射到透明度范围 0.4 - 0.01
            const opacity = Math.max(0.01, Math.min(0.4, (0.4 - (visibility / 37) * 0.39)));

            return `linear-gradient(to bottom, rgba(255, 255, 255, ${opacity}) 50%, rgba(0, 0, 0, ${opacity}) 100%)`;
        }
    }
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

/* 代表能见度的渐变效果 */
.visualization {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}

.gradient-bar {
    width: 100%;
    height: 100%;
    border-radius: 15PX;
    transition: background 0.3s ease;
}
</style>
