<template>
  <BaseLayout>
    <div class="main-container">
      <div class="card register-card">
        <div class="card-body">
          <h2 class="text-center mb-4">Register</h2>
          
          <form @submit.prevent="register">
            <div class="mb-3">
              <label class="form-label">Email address</label>
              <input
                type="email"
                class="form-control"
                v-model="email"
                placeholder="Enter your email"
                required
              />
            </div>

            <div class="mb-3">
              <label class="form-label">Password</label>
              <input
                type="password"
                class="form-control"
                v-model="password"
                placeholder="Enter your password"
                required
              />
            </div>

            <div class="mb-3">
              <label class="form-label">Confirm Password</label>
              <input
                type="password"
                class="form-control"
                v-model="password2"
                placeholder="Confirm your password"
                required
              />
            </div>

            <button type="submit" class="btn btn-primary w-100 mt-2">
              Register
            </button>
          </form>

          <div class="text-center mt-4">
            <p>Do have an account? <RouterLink :to="{ name: 'login' }">Login</RouterLink></p>
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
      password2: '',
      loading: false
    }
  },
  created() {
    const authStore = useAuthStore()
    if (authStore.isLoggedIn) {
      this.$router.push({ name: 'home' })
    }
  },
  methods: {
    async register() {
      if (!this.validateForm()) return
      
      this.loading = true
      
      try {
        const authStore = useAuthStore()
        await authStore.registerRequest({
          email: this.email,
          password: this.password,
          password2: this.password2,
        });
        
        Notiflix.Notify.success(
          'Registration successful!',
          {
            timeout: 5000,
            position: 'right-bottom',
          },
        );

        this.$router.push({ name: 'login' })
        
      } catch (error) {
        Notiflix.Notify.failure(
          'Registration failed. Please check your information.',
          {
            timeout: 5000,
            position: 'right-bottom',
          },
        );
        console.error('Registration error:', error);
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
      
      if (this.password.length < 6) {
        Notiflix.Report.failure(
          'Validation Error',
          'Password must be at least 6 characters long.',
          'OK'
        );
        return false;
      }
      
      // Confirm password validation
      if (!this.password2) {
        Notiflix.Report.failure(
          'Validation Error',
          'Please confirm your password.',
          'OK'
        );
        return false;
      }
      
      if (this.password !== this.password2) {
        Notiflix.Report.failure(
          'Validation Error',
          'Passwords do not match. Please try again.',
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
  min-height: 70vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.register-card {
  width: 100%;
  max-width: 450px;
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>