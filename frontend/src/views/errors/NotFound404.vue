<template>
  <BaseLayout>
    <div class="d-flex flex-column justify-content-center align-items-center text-center mt-custom">
      <h1 class="error">404</h1>
      <div class="page">Ooops!!! The page you are looking for is not found</div>
      <RouterLink :to="{ name: 'home' }" class="btn btn-dark fw-bold mt-3">
        Back to home
      </RouterLink>
    </div>
  </BaseLayout>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";

export default {
  components: {
    BaseLayout,
  },
};
</script>

<style scoped>
.mt-custom {
  margin-top: 200px;
}

.error {
  font-size: 150px;
  color: #008b62;
  text-shadow: 1px 1px 1px #00593e, 2px 2px 1px #00593e, 3px 3px 1px #00593e,
    4px 4px 1px #00593e, 5px 5px 1px #00593e, 6px 6px 1px #00593e,
    7px 7px 1px #00593e, 8px 8px 1px #00593e, 25px 25px 8px rgba(0, 0, 0, 0.2);
}

.page {
  font-size: 20px;
  font-weight: 600;
  color: #444;
}
</style>
