<template>
    <article class="p-10 flex flex-wrap justify-evenly">
        <div v-for="book in books" :key="book.id" class="mb-7 relative grid w-172 bg-transparent border border-white rounded-lg shadow">
            <a href="#" class="flex flex-col items-center rounded-lg shadow md:flex-row md:max-w-4xl hover:bg-gray-100 bg-transparent dark:hover:bg-gray-700">
                <img class="object-cover w-full rounded-t-lg md:h-85 md:w-64 md:rounded-none md:rounded-s-lg" :src="getImageUrl(book.publication_image)" alt="">
                <div class="flex flex-col justify-between p-4 leading-normal">
                    <h5 class=" absolute top-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white">{{ book.publication_name }}</h5>
                    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{{ truncateDescription(book.publication_description) }}</p>
                    <div class="items-center mt-2.5 mb-5">
                        <div class="flex items-center justify-between">
                            <span class="text-2xl font-bold text-gray-900 dark:text-white">&#8377 {{ book.publication_price }}</span>
                            <a href="#" class="absolute bottom-4 right-5 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Add to cart</a>
                        </div>
                        <span :class="getPriceTagClasses(book.publication_price_tag)" class="-ml-1 text-xs font-semibold px-2.5 py-0.5 rounded ms-3">{{ book.publication_price_tag }}</span>
                        <div class="absolute bottom-4 flex flex-grid mt-10">
                            <div class="flex items-center space-x-1 rtl:space-x-reverse">
                                <svg class="w-4 h-4 text-yellow-300" fill="currentColor" viewBox="0 0 22 20">
                                    <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                </svg>
                                <svg class="w-4 h-4 text-yellow-300" fill="currentColor" viewBox="0 0 22 20">
                                    <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                </svg>
                                <svg class="w-4 h-4 text-yellow-300" fill="currentColor" viewBox="0 0 22 20">
                                    <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                </svg>
                                <svg class="w-4 h-4 text-yellow-300" fill="currentColor" viewBox="0 0 22 20">
                                    <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                </svg>
                                <svg class="w-4 h-4 text-gray-200 dark:text-gray-600" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                                    <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                                </svg>
                            </div>
                            <span class="bg-blue-100 text-blue-800 text-xs font-semibold px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800 ms-3">4.0</span>
                    </div>
                </div>
                </div>
            </a>
        </div>
    </article>
</template>



<script setup lang="ts">
import {ref, onMounted} from "vue";
import apiClient from "../plugins/axios";

const books = ref([]);

const fetchBooks = async () => {
    try{
        const response = await apiClient.get('/api/publication');
        books.value = response.data;
        console.log(books)
    } catch(error) {
        console.error("Error fetching books:", error)
    }
};

const getImageUrl = (imagePath: string) => {
  return `http://localhost:8000/${imagePath}`;
};

const truncateDescription = (description: string, maxLength = 100) => {
  if (description.length <= maxLength) {
    return description;
  }
  return description.substring(0, maxLength) + '...';
};

const getPriceTagClasses = (priceTag: string) => {
  switch (priceTag) {
    case 'Best Seller':
      return 'bg-green-200 text-green-900';
    case 'In Stock':
      return 'bg-orange-200 text-orange-900';
    case 'Pre-Booking':
      return 'bg-red-200 text-red-900';
    default:
      return 'bg-blue-200 text-blue-900';
  }
};

onMounted(() => {
    fetchBooks();
});
</script>
