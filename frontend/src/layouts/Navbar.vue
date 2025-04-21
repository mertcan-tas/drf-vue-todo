<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <RouterLink :to="{ name: 'home' }"  class="navbar-brand ps-3">Todo App</RouterLink>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <RouterLink :to="{ name: 'home' }" class="nav-link" exact-active-class="active" aria-current="page">Home</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink v-if="isLoggedIn" :to="{ name: 'dashboard' }" class="nav-link" exact-active-class="active">My Todos</RouterLink>
          </li>
        </ul>
        <div v-if="!isLoggedIn" class="d-flex">
          <RouterLink :to="{ name: 'login' }" class="btn btn-outline-success me-2" type="button">Login</RouterLink>
          <RouterLink  :to="{ name: 'register' }" class="btn btn-primary" type="button">Sign Up</RouterLink>
        </div>
        <div v-else class="d-flex">
          <button @click="logout" class="btn btn-outline-danger me-2" type="button">Logout</button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import LogoutMixin from "@/mixins/LogoutMixin";
import { useAuthStore } from "@/plugins/stores/auth";
import { storeToRefs } from "pinia";
import { RouterLink } from "vue-router";

export default {
  mixins: [LogoutMixin],
  inject: ["state"],
  data() {
    return {
      userData: {
        email: "",
      },
    };
  },
  created() {
    this.authStore = useAuthStore();
    if (this.authStore.isLoggedIn) {
      this.fetchUserData();
    }
  },
  methods: {
    async fetchUserData() {
      try {
        await this.authStore.getUserData();
        const { userData } = storeToRefs(this.authStore);
        this.userData = userData.value;
      } catch (error) {
        console.error("Kullanıcı bilgileri alınamadı:", error);
      }
    },
  },
};
</script>
