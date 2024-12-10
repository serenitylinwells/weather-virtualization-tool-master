<template>
  <div id="app">
    <header>
      <h2 class="logo">Weather Virtualization Tool</h2>
      <nav class="navigation">
        <!-- 未登录时显示 -->
        <div class="buttons" v-if="!isLoggedIn">
          <router-link to="/" class="btnWeather">Weather</router-link>
          <router-link to="/setting" class="btnSetting">Setting</router-link>
          <router-link to="/login" class="btnLogin-popup">Login/Register</router-link>
        </div>
        <!-- 已登录时显示 -->
        <div class="user-info" v-else>
          <router-link to="/" class="btnWeather">Weather</router-link>
          <router-link to="/setting" class="btnSetting">Setting</router-link>
          <span class="username">Hello, {{ username }}</span>
          <button class="btnLogout" @click="handleLogout">Logout</button>
        </div>
      </nav>
    </header>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      username: "",
    };
  },
  computed: {
    isLoggedIn() {
      return !!localStorage.getItem("token");
    },
  },
  mounted() {
    this.updateUserState();
  },
  methods: {
    updateUserState() {
      const token = localStorage.getItem("token");
      if (token) {
        try {
          const payload = JSON.parse(atob(token.split(".")[1]));
          this.username = payload.username;
        } catch (error) {
          console.error("Invalid token:", error);
          this.username = "";
        }
      } else {
        this.username = "";
      }
    },
    handleLogout() {
      localStorage.removeItem("token");
      this.username = "";
      this.$router.push("/login");
      setTimeout(() => location.reload(), 100);
    },
  },
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

html,
body {
  overflow: hidden;
}

header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 1.3rem 8%;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 100;
  background-color: rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(1.9rem);
}

header i {
  font-size: 3rem;
  color: #fff;
}

header::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, #dddddd4d, transparent);
  transition: 0.4s;
  pointer-events: none;
}

header:hover::after {
  left: 40%;
}

.logo {
  font-size: 2rem;
  color: #fff;
  pointer-events: none;
}

.navigation a {
  position: relative;
  font-size: 1.2rem;
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  margin-left: 2.5rem;
}

.navigation .btnWeather,
.navigation .btnSetting {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  width: 6rem;
  height: 3rem;
  background: transparent;
  border: 0.13rem solid #fff;
  outline: none;
  border-radius: 1.5rem;
  cursor: pointer;
  font-size: 1.3rem;
  color: #fff;
  font-weight: 500;
  margin-left: 3rem;
  transition: 0.5s;
  text-decoration: none;
}

.navigation .btnLogin-popup {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  width: 9rem;
  height: 3rem;
  background: transparent;
  border: 0.13rem solid #fff;
  outline: none;
  border-radius: 1.5rem;
  cursor: pointer;
  font-size: 1.3rem;
  color: #fff;
  font-weight: 500;
  margin-left: 3rem;
  transition: 0.5s;
  text-decoration: none;
}

.navigation .btnLogin-popup:hover,
.navigation .btnWeather:hover,
.navigation .btnSetting:hover {
  background: #fff;
  color: #162938;
}

.user-info {
  display: flex;
  align-items: center;
}

.username {
  margin-right: 1rem;
  font-weight: bold;
  color: #fff;
  margin-left: 20px;
}

.btnLogout {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 15px;
  background-color: rgb(255, 77, 77);
  color: white;
  cursor: pointer;
  transition: 0.3s;
}

.btnLogout:hover {
  background-color: rgb(241, 98, 98);
}
</style>
