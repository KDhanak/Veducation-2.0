<script setup lang = "ts">
    import {ref, onMounted} from "vue";
    import carouselImage1 from "../assets/Screenshot 2024-03-22 164932.png"
    import carouselImage2 from "../assets/Screenshot 2024-03-22 200626.png"
    import carouselImage3 from "../assets/Screenshot 2024-03-22 200741.png"
    import carouselImage4 from "../assets/Screenshot 2024-03-22 200902.png"
    import carouselImage5 from "../assets/Screenshot 2024-03-22 200953.png"

const images = [
  carouselImage1,
  carouselImage2,
  carouselImage3,
  carouselImage4,
  carouselImage5,
];

const currentSlide = ref(0);

const nextSlide = () => {
    currentSlide.value = (currentSlide.value + 1) % images.length;
};

const prevSlide = () => {
    currentSlide.value = (currentSlide.value - 1 + images.length) % images.length
};
</script>

<template>
    <section class="p-20">
        <div id="default-carousel" class="relative grid" data-carousel="slide">
        <!-- Carousel wrapper -->
            <div class="relative flex justify-self-center overflow-hidden rounded-lg h-128 w-3/5">
                <!-- Items -->
                <div v-for = "(image,index) in images" :key = "index" class="duration-700 ease-in-out absolute inset-0 transition-opacity" :class="{'opacity-0':currentSlide !==index, 'opacity-100':currentSlide === index}">
                    <img :src="image" class="absolute rounded-xl block -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2 size-full" alt="...">
                </div>
            </div>

            <!-- Slider indicators -->
            <div class="absolute z-30 flex -translate-x-1/2 -bottom-5 left-1/2 space-x-3 rtl:space-x-reverse">
                <button v-for="(image, index) in images" :key="index" type="button" class="w-3 h-3 bg-white rounded-full" :aria-current="currentSlide === index ? 'true' : 'false'" :aria-label="'Slide ' + (index + 1)" @click="currentSlide = index" :class="{'bg-white': currentSlide === index, 'bg-gray-400': currentSlide !== index }"></button>
            </div>

            <!-- Slider controls -->
            <button type="button" @click="prevSlide" class="absolute top-0 start-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none" data-carousel-prev>
                <span class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white group-hover:bg-white/50  group-focus:ring-4 group-focus:ring-white group-focus:outline-none">
                    <svg class="w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180" aria-hidden="false" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 1 1 5l4 4"/>
                    </svg>
                    <span class="sr-only">Previous</span>
                </span>
            </button>
            <button type="button" @click="nextSlide" class="absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none" data-carousel-next>
                <span class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white group-hover:bg-white/50  group-focus:ring-4 group-focus:ring-white group-focus:outline-none">
                    <svg class="w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180" aria-hidden="false" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
                    </svg>
                <span class="sr-only">Next</span>
                </span>
            </button>
        </div>

    </section>
</template>