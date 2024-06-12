<template>
    <!-- component -->
    <div class="bg-white dark:bg-gray-900">
        <div class="flex justify-center h-screen">
            <div class="hidden bg-cover lg:block lg:w-2/3" id="imageClass">
                <div class="flex items-center h-full px-20 bg-gray-900 bg-opacity-40">
                    <div>
                        <h2 class="text-4xl font-bold text-bgSaffron">Veducation</h2>
                        <p class="max-w-xl mt-3 text-gray-100 text-justify font-medium">Learn about vedic science, history, philosophy & culture in details. With Prateeik Prajapati, who has been reading and researching collective psychologies of world civilisations since last 7 years. </p>
                        <p class="max-w-xl mt-3 text-gray-100 text-justify font-medium">Now he has decided to share all that invaluable knowledge with the world through his talks and sessions in schools, colleges, corporates, villages & online through Youtube & social media.</p>
                    </div>
                </div>
            </div>
                
            <div class="flex items-center w-full max-w-md px-6 mx-auto lg:w-2/6">
                <div class="flex-1">
                    <div class="text-center">
                        <h2 class="text-4xl font-bold text-center text-gray-700 dark:text-bgSaffron">Veducation</h2>
                        
                        <p class="mt-3 text-gray-500 dark:text-gray-300">Sign up to join us</p>
                    </div>

                    <a href="#" class="flex items-center justify-center mt-4 text-white rounded-lg transition-colors duration-200 transform bg-gray-200 shadow-md hover:bg-gray-300">
                        <div class="px-4 py-3">
                            <svg class="h-6 w-6" viewBox="0 0 40 40">
                                <path d="M36.3425 16.7358H35V16.6667H20V23.3333H29.4192C28.045 27.2142 24.3525 30 20 30C14.4775 30 10 25.5225 10 20C10 14.4775 14.4775 9.99999 20 9.99999C22.5492 9.99999 24.8683 10.9617 26.6342 12.5325L31.3483 7.81833C28.3717 5.04416 24.39 3.33333 20 3.33333C10.7958 3.33333 3.33335 10.7958 3.33335 20C3.33335 29.2042 10.7958 36.6667 20 36.6667C29.2042 36.6667 36.6667 29.2042 36.6667 20C36.6667 18.8825 36.5517 17.7917 36.3425 16.7358Z" fill="#FFC107"/>
                                <path d="M5.25497 12.2425L10.7308 16.2583C12.2125 12.59 15.8008 9.99999 20 9.99999C22.5491 9.99999 24.8683 10.9617 26.6341 12.5325L31.3483 7.81833C28.3716 5.04416 24.39 3.33333 20 3.33333C13.5983 3.33333 8.04663 6.94749 5.25497 12.2425Z" fill="#FF3D00"/>
                                <path d="M20 36.6667C24.305 36.6667 28.2167 35.0192 31.1742 32.34L26.0159 27.975C24.3425 29.2425 22.2625 30 20 30C15.665 30 11.9842 27.2359 10.5975 23.3784L5.16254 27.5659C7.92087 32.9634 13.5225 36.6667 20 36.6667Z" fill="#4CAF50"/>
                                <path d="M36.3425 16.7358H35V16.6667H20V23.3333H29.4192C28.7592 25.1975 27.56 26.805 26.0133 27.9758C26.0142 27.975 26.015 27.975 26.0158 27.9742L31.1742 32.3392C30.8092 32.6708 36.6667 28.3333 36.6667 20C36.6667 18.8825 36.5517 17.7917 36.3425 16.7358Z" fill="#1976D2"/>
                            </svg>
                        </div>
                    <h1 class="px-4 py-3 w-5/6 text-center text-gray-600 font-bold">Sign up with Google</h1>
                    </a>

                    <div class="mt-8">
                        <form>
                            <div class="mt-4">
                                <div>
                                    <label for="username" class="block mb-2 text-sm text-gray-600 dark:text-gray-200">Username</label>
                                    <input type="text" v-model="username" name="username" id="fname" placeholder="Create a username" class="block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                                </div>
                            </div>
                            <div class="mt-4">
                                <div>
                                    <label for="first_name" class="block mb-2 text-sm text-gray-600 dark:text-gray-200">First Name</label>
                                    <input type="text" v-model="first_name" name="first_name" id="fname" placeholder="First Name" class="block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                                </div>
                            </div>
                            
                            <div class="mt-4">
                                <div>
                                    <label for="last_name" class="block mb-2 text-sm text-gray-600 dark:text-gray-200">Last Name</label>
                                    <input type="text" v-model="last_name" name="last_name" id="lname" placeholder="Last Name" class="block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                                </div>
                            </div>

                            <div class="mt-4">
                                <div>
                                    <label for="email" class="block mb-2 text-sm text-gray-600 dark:text-gray-200">Email Address</label>
                                    <input type="email" v-model="email" name="email" id="email" placeholder="example@example.com" class="block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                                </div>
                            </div>

                            <div class="mt-4">
                                <div>
                                    <label for="phone_number" class="block mb-2 text-sm text-gray-600 dark:text-gray-200">Phone Number</label>
                                    <input type="tel" v-model="phone_number" name="phone_number" id="phone_number" placeholder="Phone Number" class="block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                                </div>
                            </div>

                            <div class="mt-4">
                                <div class="flex justify-between mb-2">
                                    <label for="password" class="text-sm text-gray-600 dark:text-gray-200">Password</label>
                                </div>

                                <input type="password" v-model="password" name="password" id="password" placeholder="Your Password" class="block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                            </div>

                            <div class="mt-4">
                                <button
                                    class="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-blue-500 rounded-md hover:bg-blue-400 focus:outline-none focus:bg-blue-400 focus:ring focus:ring-blue-300 focus:ring-opacity-50">
                                    Sign up
                                </button>
                            </div>

                        </form>

                        <p class="mt-6 text-sm text-center text-gray-400">Already have an account? <a :href ="loginUrl" target="_blank" class="text-blue-500 focus:outline-none focus:underline hover:underline cursor-pointer">Sign in</a>.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script lang="ts" setup>
import {ref, onMounted, computed} from "vue";
import axios from "axios";

const loginUrl = computed(() => `${import.meta.env.VITE_BASE_URL}/login`);


const username = ref('');
const first_name = ref('');
const last_name = ref('');
const email = ref('');
const phone_number = ref('');
const password = ref('');

const register = async () => {
    try {
        const response = await axios.post(`${import.meta.env.VITE_BACKEND_BASE_URL}/authmanagement/registration`, {
            username: username.value,
            first_name: first_name.value,
            last_name: last_name.value,
            email: email.value,
            phone_number: phone_number.value,
            password: password.value,
        });
        console.log("Registration Successful:", response.data);
    } catch (error) {
        console.error("Error during registration", error.repsonse.data)
    }

    return {
        username, first_name, last_name, email, phone_number, password
    };
};



</script>

<style scoped>
#imageClass {
    background-image: url("../assets/9744893-ram-mandir-krishna-image.jpg");
}
</style>