<template>
    <div class="background"></div>
    <div class="container" ref="container">
        <div class="form-box login" ref="loginBox">
            <form @submit.prevent="handleLogin">
                <h1>Login</h1>
                <div class="input-box">
                    <input v-model="loginForm.username" type="text" placeholder="Phone Number (11 digits)" required />
                    <i class="bx bxs-user"></i>
                </div>
                <div class="input-box">
                    <input v-model="loginForm.password" type="password" placeholder="Password" required />
                    <i class="bx bxs-lock-alt"></i>
                </div>
                <div class="forgot-link">
                    <a href="#">Forgot password?</a>
                </div>
                <button type="submit" class="btn">Login</button>
            </form>
        </div>
        <div class="form-box register" ref="registerBox">
            <form @submit.prevent="handleRegister">
                <h1>Registration</h1>
                <div class="input-box">
                    <input v-model="registerForm.username" type="text" placeholder="Phone Number (11 digits)" required />
                    <i class="bx bxs-user"></i>
                </div>
                <div class="input-box">
                    <input v-model="registerForm.password" type="password" placeholder="Password" required />
                    <i class="bx bxs-lock-alt"></i>
                </div>
                <button type="submit" class="btn">Register</button>
            </form>
        </div>
        <div class="toggle-box">
            <div class="toggle-panel toggle-left">
                <h1>Hello, Welcome!</h1>
                <p>Don't have an account?</p>
                <button class="btn register-btn" @click="switchToRegister">Register</button>
            </div>
            <div class="toggle-panel toggle-right">
                <h1>Welcome Back!</h1>
                <p>Already have an account?</p>
                <button class="btn login-btn" @click="switchToLogin">Login</button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            loginForm: {
                username: "",
                password: "",
            },
            registerForm: {
                username: "",
                password: "",
            },
        };
    },
    methods: {
        switchToRegister() {
            this.$refs.container.classList.add("active");
            this.$refs.loginBox.style.visibility = "hidden";
            this.$refs.loginBox.style.opacity = "0";
            this.$refs.registerBox.style.visibility = "visible";
            this.$refs.registerBox.style.opacity = "1";
        },
        switchToLogin() {
            this.$refs.container.classList.remove("active");
            this.$refs.registerBox.style.visibility = "hidden";
            this.$refs.registerBox.style.opacity = "0";
            this.$refs.loginBox.style.visibility = "visible";
            this.$refs.loginBox.style.opacity = "1";
        },

        validatePhoneNumber(phone) {
            const phoneRegex = /^[0-9]{11}$/; // 匹配 11 位数字
            return phoneRegex.test(phone);
        },

        async handleRegister() {
            try {
                const response = await axios.post("http://127.0.0.1:8081/weatherTool/register-api/register", {
                    username: this.registerForm.username,
                    detail: this.registerForm.password,
                });
                if (response.data.code === 0) {
                    alert("Registration successful! Please login.");
                    this.switchToLogin();
                } else {
                    alert(response.data.msg);
                }
            } catch (error) {
                console.error("Registration failed:", error);
                alert("Registration failed. Please try again.");
            }
        },
        async handleLogin() {
            try {
                const response = await axios.get("http://127.0.0.1:8081/weatherTool/register-api/login", {
                    params: {
                        username: this.loginForm.username,
                        detail: this.loginForm.password,
                    },
                });
                if (response.data.code === 0) {
                    const token = response.data.data.token;
                    localStorage.setItem("token", token); // 保存 Token
                    alert("Login successful!");
                    this.$router.push("/");
                    setTimeout(() => location.reload(), 100);
                } else {
                    alert(response.data.msg);
                }
            } catch (error) {
                console.error("Login failed:", error);
                alert("Login failed. Please try again.");
            }
        },
    },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap");

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}

body {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background: linear-gradient(90deg, #e2e2e2, #c9d6ff);
}

.background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: url(../assets/cloudy.jpg) no-repeat;
    background-size: cover;
    z-index: -1;
}

.container {
    position: relative;
    width: 850px;
    height: 550px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 30px;
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.2);
    margin: 20px;
    overflow: hidden;
}

.form-box {
    position: absolute;
    right: 0;
    width: 50%;
    height: 100%;
    background: rgba(255, 255, 255, 0.2);
    display: flex;
    align-items: center;
    color: #333;
    text-align: center;
    padding: 40px;
    z-index: 1;
    transition: 0.6s ease-in-out 1.2s, visibility 0s 1s;
}

.container.active .form-box {
    right: 50%;
}

.form-box.register {
    visibility: hidden;
}

.container.active .form-box.register {
    visibility: visible;
}

.form-box.login {
    visibility: visible;
    opacity: 1;
}

.form-box.register {
    visibility: hidden;
    opacity: 0;
}

form {
    width: 100%;
}

.container h1 {
    font-size: 36px;
    margin: -10px 0;
}

.input-box {
    position: relative;
    margin: 30px 0;
}

.input-box input {
    width: 100%;
    padding: 13px 50px 13px 20px;
    background: #eee;
    border-radius: 8px;
    border: none;
    outline: none;
    font-size: 16px;
    color: #333;
    font-weight: 500;
}

.input-box input::placeholder {
    color: #888;
    font-weight: 400;
}

.input-box i {
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 20px;
    color: #888;
}

.forgot-link {
    margin: -15px 0 15px;
}

.forgot-link a {
    font-size: 14.5px;
    color: #333;
    text-decoration: none;
}

.btn {
    width: 100%;
    height: 48px;
    background-color: #7494ec;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border: none;
    cursor: pointer;
    font-size: 16px;
    color: #fff;
    font-weight: 600;
}

.container p {
    font-size: 14.5px;
    margin: 15px 0;
}

.social-icons {
    display: flex;
    justify-content: center;
}

.social-icons a {
    display: inline-flex;
    padding: 10px;
    border: 2px solid #ccc;
    border-radius: 8px;
    font-size: 24px;
    color: #333;
    text-decoration: none;
    margin: 0 8px;
}

.toggle-box {
    position: absolute;
    width: 100%;
    height: 100%;
}

.toggle-box::before {
    content: "";
    position: absolute;
    left: -250%;
    width: 300%;
    height: 100%;
    background: #7494ec;
    border-radius: 150px;
    z-index: 2;
    transition: 1.8s ease-in-out;
}

.container.active .toggle-box::before {
    left: 50%;
}

.toggle-panel {
    position: absolute;
    width: 50%;
    height: 100%;
    color: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 2;
    transition: 0.6s ease-in-out;
}

.toggle-panel.toggle-left {
    left: 0;
    transition-delay: 1.2s;
}

.container.active .toggle-panel.toggle-left {
    left: -50%;
    transition-delay: 0.6s;
}

.toggle-panel.toggle-right {
    right: -50%;
    transition-delay: 0.6s;
}

.container.active .toggle-panel.toggle-right {
    right: 0;
    transition-delay: 1.2s;
}

.toggle-panel p {
    margin-bottom: 20px;
}

.toggle-panel .btn {
    width: 160px;
    height: 46px;
    background: transparent;
    border: 2px solid #fff;
    box-shadow: none;
    outline: none;
}

@media screen and (max-width: 650px) {
    .container {
        height: calc(100vh - 40px);
    }

    .form-box {
        bottom: 0;
        width: 100%;
        height: 70%;
    }

    .container.active .form-box {
        right: 0;
        bottom: 30%;
    }

    .toggle-box::before {
        left: 0;
        top: -270%;
        width: 100%;
        height: 300%;
    }

    .container.active .toggle-box::before {
        left: 0;
        top: 70%;
    }

    .toggle-panel {
        width: 100%;
        height: 30%;
    }

    .toggle-panel.toggle-left {
        top: 0;
    }

    .container.active .toggle-panel.toggle-left {
        left: 0;
        top: -30%;
    }

    .toggle-panel.toggle-right {
        right: 0;
        bottom: -30%;
    }

    .container.active .toggle-panel.toggle-right {
        bottom: 0;
    }
}

@media screen and (max-width: 400px) {
    .form-box {
        padding: 20px;
    }

    .toggle-panel h1 {
        font-size: 30px;
    }
}
</style>