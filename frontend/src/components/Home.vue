<script setup lang="ts">
import NavBar from "../sub-components/NavBar.vue";
import Carousel from "../sub-components/Carousel.vue";
import ProductCard from "../sub-components/ProductCard.vue"
</script>

<template>
  <div>
    <NavBar />
    <Carousel />
    <h1 class="pt-5 flex justify-center font-semibold text-4xl">Our Books</h1>
    <ProductCard />
  </div>
</template>
