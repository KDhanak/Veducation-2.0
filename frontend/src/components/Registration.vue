<template>
    <!-- component -->
    <div class="bg-white dark:bg-gray-900">
        <div class="flex justify-center h-screen">
            <div class="hidden bg-cover lg:block lg:w-2/3" id="imageClass">
                <div class="flex items-center h-full px-20 bg-gray-900 bg-opacity-60">
                    <div>
                        <h2 class="text-4xl font-bold text-bgSaffron">Veducation</h2>
                        <p class="max-w-xl mt-3 text-gray-100 text-justify font-medium">Learn about vedic science,
                            history, philosophy & culture in details. With Prateeik Prajapati, who has been reading and
                            researching collective psychologies of world civilisations since last 7 years. </p>
                        <p class="max-w-xl mt-3 text-gray-100 text-justify font-medium">Now he has decided to share all
                            that invaluable knowledge with the world through his talks and sessions in schools,
                            colleges, corporates, villages & online through Youtube & social media.</p>
                    </div>
                </div>
            </div>

            <div class="flex items-center w-full max-w-md px-6 mx-auto lg:w-2/6">
                <div class="flex-1">
                    <div v-if="displayMessage" :class="warningTheme"
                        class="flex items-center p-4 mb-4 text-sm border rounded-lg bg-red-50 dark:bg-gray-800"
                        role="alert">
                        <svg class="flex-shrink-0 inline w-4 h-4 me-3" aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                            <path
                                d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
                        </svg>
                        <span class="sr-only">Info</span>
                        <div>
                            <span class="font-medium"></span> {{ displayMessage }}
                        </div>
                    </div>
                    <div class="text-center">
                        <h2 class="text-4xl font-bold text-center text-gray-700 dark:text-bgSaffron">Veducation</h2>

                        <p class="mt-3 text-gray-500 dark:text-gray-300">Sign up to join us</p>
                    </div>

                    <a href="#"
                        class="flex items-center justify-center mt-4 text-white rounded-lg transition-colors duration-200 transform bg-gray-200 shadow-md hover:bg-gray-300">
                        <div class="px-4 py-3">
                            <svg class="h-6 w-6" viewBox="0 0 40 40">
                                <path
                                    d="M36.3425 16.7358H35V16.6667H20V23.3333H29.4192C28.045 27.2142 24.3525 30 20 30C14.4775 30 10 25.5225 10 20C10 14.4775 14.4775 9.99999 20 9.99999C22.5492 9.99999 24.8683 10.9617 26.6342 12.5325L31.3483 7.81833C28.3717 5.04416 24.39 3.33333 20 3.33333C10.7958 3.33333 3.33335 10.7958 3.33335 20C3.33335 29.2042 10.7958 36.6667 20 36.6667C29.2042 36.6667 36.6667 29.2042 36.6667 20C36.6667 18.8825 36.5517 17.7917 36.3425 16.7358Z"
                                    fill="#FFC107" />
                                <path
                                    d="M5.25497 12.2425L10.7308 16.2583C12.2125 12.59 15.8008 9.99999 20 9.99999C22.5491 9.99999 24.8683 10.9617 26.6341 12.5325L31.3483 7.81833C28.3716 5.04416 24.39 3.33333 20 3.33333C13.5983 3.33333 8.04663 6.94749 5.25497 12.2425Z"
                                    fill="#FF3D00" />
                                <path
                                    d="M20 36.6667C24.305 36.6667 28.2167 35.0192 31.1742 32.34L26.0159 27.975C24.3425 29.2425 22.2625 30 20 30C15.665 30 11.9842 27.2359 10.5975 23.3784L5.16254 27.5659C7.92087 32.9634 13.5225 36.6667 20 36.6667Z"
                                    fill="#4CAF50" />
                                <path
                                    d="M36.3425 16.7358H35V16.6667H20V23.3333H29.4192C28.7592 25.1975 27.56 26.805 26.0133 27.9758C26.0142 27.975 26.015 27.975 26.0158 27.9742L31.1742 32.3392C30.8092 32.6708 36.6667 28.3333 36.6667 20C36.6667 18.8825 36.5517 17.7917 36.3425 16.7358Z"
                                    fill="#1976D2" />
                            </svg>
                        </div>
                        <h1 class="px-4 py-3 w-5/6 text-center text-gray-600 font-bold">Sign up with Google</h1>
                    </a>

                    <div class="mt-8">
                        <form @submit.prevent="handleSubmit()">
                            <div class="mt-4">
                                <div>
                                    <label for="first_name"
                                        class="block mb-2 text-sm text-gray-600 dark:text-gray-200">First Name</label>
                                    <input type="text" v-model="form.first_name" name="first_name" id="fname"
                                        placeholder="First Name"
                                        class="block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                                    <div v-if="validationErrors.first_name" class="text-red-500 text-xs">{{
                                        validationErrors.first_name }}</div>
                                </div>
                            </div>

                            <div class="mt-4">
                                <div>
                                    <label for="last_name"
                                        class="block mb-2 text-sm text-gray-600 dark:text-gray-200">Last Name</label>
                                    <input type="text" v-model="form.last_name" name="last_name" id="lname"
                                        placeholder="Last Name"
                                        class="block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                                    <div v-if="validationErrors.last_name" class="text-red-500 text-xs">{{
                                        validationErrors.last_name }}</div>
                                </div>
                            </div>

                            <div class="mt-4">
                                <div>
                                    <label for="email" class="block mb-2 text-sm text-gray-600 dark:text-gray-200">Email
                                        Address</label>
                                    <input type="text" v-model="form.email" name="email" id="email"
                                        placeholder="example@example.com"
                                        class="block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                                    <div v-if="validationErrors.email" class="text-red-500 text-xs">{{
                                        validationErrors.email }}</div>
                                </div>
                            </div>

                            <div class="mt-4">
                                <div>
                                    <label for="phone_number"
                                        class="block mb-2 text-sm text-gray-600 dark:text-gray-200">Phone Number</label>
                                    <input type="tel" v-model="form.phone_number" name="phone_number" id="phone_number"
                                        placeholder="Phone Number"
                                        class="block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                                    <div v-if="validationErrors.phone_number" class="text-red-500 text-xs">{{
                                        validationErrors.phone_number }}</div>
                                </div>
                            </div>

                            <div class="mt-4">
                                <div class="flex justify-between mb-2">
                                    <label for="password"
                                        class="text-sm text-gray-600 dark:text-gray-200">Password</label>
                                </div>

                                <input type="password" v-model="form.password" name="password" id="password"
                                    placeholder="Your Password"
                                    class="block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                                <div v-if="validationErrors.password" class="text-red-500 text-xs">{{
                                    validationErrors.password }}</div>
                            </div>

                            <div class="mt-4">
                                <button
                                    class="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-blue-500 rounded-md hover:bg-blue-400 focus:outline-none focus:bg-blue-400 focus:ring focus:ring-blue-300 focus:ring-opacity-50">
                                    Sign up
                                </button>
                            </div>

                        </form>

                        <p class="mt-6 text-sm text-center text-gray-400">Already have an account? <a :href="loginUrl"
                                target="_blank"
                                class="text-blue-500 focus:outline-none focus:underline hover:underline cursor-pointer">Sign
                                in</a>.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { ref, computed } from "vue";
import axios from "axios";
import apiClient from "../plugins/axios";
import Cookies from "js-cookie";
import { useRouter } from "vue-router";

const loginUrl = computed(() => `${import.meta.env.VITE_BASE_URL}/login`);
const router = useRouter();

const errorRef = ref<string | null>(null);
const successMessage = ref<string | null>(null);
const warningThemeValue = ref<boolean | null>(null);

type FormFields = {
    first_name: string;
    last_name: string;
    email: string;
    phone_number: string;
    password: string;
}

const form = ref<FormFields>({
    first_name: "",
    last_name: "",
    email: "",
    phone_number: "",
    password: "",
});

const validationErrors = ref({
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    phone_number: "",
    password: "",

})

const validateField = (field: string, value: string) => {
    switch (field) {
        case "email":
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            validationErrors.value.email = !emailPattern.test(value) ? "Enter a valid email address." : "";
            break;
        case "password":
            validationErrors.value.password = value.length <= 8 ? "Password must be at least 8 characters long." : "";
            break;
        case "first_name":
        case "last_name":
            const namePattern = /^[A-Za-z]+$/;
            validationErrors.value[field] = !namePattern.test(value) ? "Only alphabets are allowed" : "";
            break;
        case "phone_number":
            const numberPattern = /^(?:(?:\+91|91|0)[-\s]?)?[6-9]\d{9}$/;
            validationErrors.value.phone_number = !numberPattern.test(value) ? "Please enter a valid phone number" : "";
    }
}

const handleSubmit = () => {
    Object.keys(form.value).forEach((key) => {
        validateField(key, String(form.value[key as keyof typeof form.value]));
    });

    if (Object.values(validationErrors.value).every((error) => error === "")) {
        registerUser();
    } else {
        errorRef.value = "Please correct the errors in the form";
    }
};

const registerUser = async () => {
    errorRef.value = null;
    successMessage.value = null;

    try {
        const response = await apiClient.post('/api/register', form.value);
        if (response.status === 201) {
            Cookies.set("access_token", response.data.access, { expires: 0.003, secure: true });
            Cookies.set("refresh_token", response.data.refresh, { expires: 7, secure: true }); 
            
            successMessage.value = "User registered successfully!";
            Object.keys(form.value).forEach((key) => {
                form.value[key as keyof typeof form.value] = "";
            });

            router.push({name:"Home"})

        }
    } catch (err) {
        if (axios.isAxiosError(err) && err.response) {
            console.log(err.response);
            const emailError = err.response.data.email ? err.response.data.email[0] : null;

            if (emailError) {
                errorRef.value = "The username and email are already registered.";
            } else {
                errorRef.value = emailError || "Unknown error";
            }
        } else {
            errorRef.value = "An unexpected error occurred";
        }
        console.log(errorRef.value);
        router.push({name:"Home"})
    }

    return {
        form, error: errorRef, registerUser,
    };
};

const displayMessage = computed(() => {
    if (errorRef.value) {
        warningThemeValue.value = false
        return typeof errorRef.value === "string" ? errorRef.value : "An expected error occurred";
    }
    else {
        warningThemeValue.value = true
        return successMessage.value;
    }
})

const warningTheme = computed(() => {
    if (warningThemeValue.value) {
        return "text-green-800 border-green-300 bg-green-50 dark:text-green-400 dark:border-green-800";
    } else {
        return "text-red-800 border-red-300 bg-red-50 dark:text-red-400 dark:border-red-800";
    }
})

</script>

<style scoped>
#imageClass {
    background-image: url("../assets/rammandir-1024x683.jpg");
}
</style>
