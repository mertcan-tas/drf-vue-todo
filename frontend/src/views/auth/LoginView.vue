<template>
  <BaseLayout>
    <div class="main-container">
      <div class="card login-card">
        <div class="card-body">
          <h2 class="text-center mb-4">Login</h2>
          
          <form @submit.prevent="login">
            <div class="mb-3">
              <label class="form-label">Email address</label>
              <input
                v-model="email"
                type="email"
                class="form-control"
                placeholder="Enter your email"
                required
              />
            </div>

            <div class="mb-3">
              <label class="form-label">Password</label>
              <input
                v-model="password"
                type="password"
                class="form-control"
                placeholder="Enter your password"
                required
              />
            </div>

            <button type="submit" class="btn btn-primary w-100 mt-2">
              Login
            </button>
          </form>

          <div class="text-center mt-4">
            <p>Don't have an account? <RouterLink :to="{ name: 'register' }">Sign Up</RouterLink></p>
          </div>
        </div>
      </div>
    </div>
  </BaseLayout>
</template>

<script>
import { useAuthStore } from '@/plugins/stores/auth'
import Notiflix from 'notiflix';
import BaseLayout from "@/layouts/BaseLayout.vue";

export default {
  components: {
    BaseLayout,
  },
  data() {
    return {
      email: '',
      password: '',
      loading: false
    }
  },
  created() {
    const authStore = useAuthStore()
    if (authStore.isLoggedIn) {
      this.$router.push({ name: 'dashboard' })
    }
  },
  methods: {
    async login() {
      if (!this.validateForm()) return
      
      this.loading = true
      
      try {
        const authStore = useAuthStore()
        await authStore.loginRequest({
          email: this.email,
          password: this.password
        });
        
        Notiflix.Notify.success(
          'Login successful!',
          {
            timeout: 5000,
            position: 'right-bottom',
          },
        );

        this.$router.push({ name: 'dashboard' })
        
      } catch (error) {
        Notiflix.Notify.failure(
          'Login failed. Please check your credentials.',
          {
            timeout: 5000,
            position: 'right-bottom',
          },
        );
        console.error('Login error:', error);
      } finally {
        this.loading = false
      }
    },
    validateForm() {
      // Email validation
      if (!this.email) {
        Notiflix.Report.failure(
          'Validation Error',
          'Email is required!',
          'OK'
        );
        return false;
      }
      
      const emailRegex = /.+@.+\..+/;
      if (!emailRegex.test(this.email)) {
        Notiflix.Report.failure(
          'Validation Error',
          'Please enter a valid email address.',
          'OK'
        );
        return false;
      }
      
      // Password validation
      if (!this.password) {
        Notiflix.Report.failure(
          'Validation Error',
          'Password is required!',
          'OK'
        );
        return false;
      }
      
      return true;
    }
  }
};
</script>

<style scoped>
.main-container {
  min-height: 60vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.login-card {
  width: 100%;
  max-width: 450px;
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>