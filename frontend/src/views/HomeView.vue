<template>
  <BaseLayout>
     <section class="hero-section">
        <div class="container">
           <h1>Stay Organized with Our Todo App</h1>
           <p>Manage your tasks efficiently and never miss a deadline again!</p>
           <RouterLink :to="{ name: 'login' }" class="btn btn-light btn-lg">Get Started</RouterLink>
        </div>
     </section>
  </BaseLayout>
</template>

<script>
  import BaseLayout from "@/layouts/BaseLayout.vue";
  import { RouterLink } from "vue-router";
  
  export default {
    components: {
      BaseLayout,
    }
  }
</script>

<style scoped>
  .hero-section {
  background: #007bff;
  color: white;
  padding: 80px 0;
  text-align: center;
  }
</style>