<template>
    <footer class="bg-light text-center text-lg-start mt-auto border-top">
      <div class="container p-4">
        <div class="row">
          <div class="col-lg-6 col-md-12 mb-4 mb-md-0">
            <h5 class="text-capitalize">Todo App</h5>
            <p>
              We strive to deliver the best experience to our users. Stay connected!
            </p>
          </div>
  
          <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
            <h5 class="text-uppercase">Links</h5>
            <ul class="list-unstyled mb-0">
              <li><RouterLink :to="{ name: 'home' }" class="text-dark">Home</RouterLink></li>
              <li><RouterLink :to="{ name: 'login' }" class="text-dark">Login</RouterLink></li>
              <li><RouterLink :to="{ name: 'register' }" class="text-dark">Register</RouterLink></li>
            </ul>
          </div>
  
          <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
            <h5 class="text-uppercase">Follow Us</h5>
            <ul class="list-unstyled mb-0">
              <li><a href="#" class="text-dark">Instagram</a></li>
              <li><a href="#" class="text-dark">Twitter</a></li>
              <li><a href="#" class="text-dark">Facebook</a></li>
            </ul>
          </div>
        </div>
      </div>
      
      <div class="text-center p-3 bg-secondary text-white bg-dark">
        © {{ new Date().getFullYear() }} Todo App — All Rights Reserved.
      </div>
    </footer>
  </template>
  
  <script setup>
  </script>
  
  <style scoped>
  footer {
    font-size: 0.95rem;
  }
  </style>
  