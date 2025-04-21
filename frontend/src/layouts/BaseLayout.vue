<template>
    <div class="d-flex flex-column min-vh-100">
        <Navbar />
        <main class="flex-grow-1">
            <slot />
        </main>
        <Footer />
    </div>
</template>

<script>
import Navbar from "@/layouts/Navbar.vue";
import Footer from "@/layouts/Footer.vue";

export default {
    components: {
        Navbar,
        Footer,
    },
};
</script>



