<template>
	<nav class=" bg-bgGrey border-gray-200">
		<div class="flex max-w-full flex-wrap items-center p-4">
			<a href="#" class="flex items-center space-x-3 rtl:space-x-reverse">
				<img :src="veducationLogo" class="h-14" alt="Veducation Logo" />
				<span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Jai Shree Ram</span>
			</a>


			<div class="mx-auto items-center justify-between w-full md:flex md:w-auto" id="navbar-user">
				<ul
					class="flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg md:space-x-10 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 bg-bgGrey">
					<li>
						<a href="#"
							class="block py-2 px-3 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 md:dark:text-blue-500"
							aria-current="page">Home</a>
					</li>
					<li>
						<a href="#"
							class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Library</a>
					</li>
					<li>
						<a href="#"
							class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Courses</a>
					</li>
					<li>
						<a href="#"
							class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Yoddha
							Store</a>
					</li>
					<li>
						<button @click="toggleDropDown('moreMenu')" id="submenu-button"
							class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">More</button>
						<div :class="{ 'hidden': !dropDownVisibleMore, 'absolute': true, 'z-50': true, 'text-base': true, 'list-none': true, 'bg-white': true, 'divide-y': true, 'divide-gray-100': true, 'rounded-lg': true, 'shadow': true, 'dark:bg-gray-700': true, 'dark:divide-gray-600': true }"
							id="submenu-dropdown">
							<ul class="py-2" aria-labelledby="submenu-button">
								<li>
									<a href="#"
										class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">
										<v-icon name="fc-link" class="mr-2" /> Join Pandav Sena </a>
								</li>
								<li>
									<a href="#"
										class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">
										<v-icon name="fc-invite" class="mr-2" /> Invite Us </a>
								</li>
								<li>
									<a href="#"
										class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">
										<v-icon name="co-location-pin" class="mr-2" /> Our Gurukuls </a>
								</li>
								<li>
									<a href="#"
										class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">
										<v-icon name="co-send" class="mr-2" /> Help us spread Dharma</a>
								</li>
								<li>
									<a href="#"
										class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"><v-icon
											name="md-contentpaste" class="mr-3" />Content Usage Policy</a>
								</li>
								<li>
									<a href="#"
										class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"><v-icon
											name="md-privacytip-outlined" class="mr-3" />Privacy Policy</a>
								</li>
								<li>
									<a href="#"
										class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"><v-icon
											name="ri-refund-2-line" class="mr-3" />Return and Refunds</a>
								</li>
								<li>
									<a href="#"
										class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"><v-icon
											name="la-shipping-fast-solid" class="mr-3" />Shipping and Delivery</a>
								</li>
								<li>
									<a href="#"
										class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"><v-icon
											name="fa-list-ul" class="mr-3" />Terms of Service</a>
								</li>
								<li>
									<a href="#"
										class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"><v-icon
											name="md-contactpage-outlined" class="mr-3" />Contact Us</a>
								</li>
								<li>
									<a href="#"
										class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"><v-icon
											name="fc-about" class="mr-3" />About Veducation</a>
								</li>
							</ul>
						</div>
					</li>
				</ul>
			</div>


			<div v-if="user" class="flex mr-10 items-center space-x-3 md:space-x-0 rtl:space-x-reverse">
				<button @click="toggleDropDown('profileMenu')" type="button"
					class="flex text-sm bg-gray-800 rounded-full md:me-0 focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600"
					id="user-menu-button" aria-expanded="false">
					<span class="sr-only">Open user menu</span>
					<img class="w-12 h-12 rounded-full" :src="profileImage" alt="user photo">
				</button>

				<!-- Dropdown menu -->
				<div :class="{ 'hidden': !dropDownVisible, 'absolute': true, 'right-2': true, 'z-50': true, 'text-base': true, 'mt-80': true, 'list-none': true, 'bg-white': true, 'divide-y': true, 'divide-gray-100': true, 'rounded-lg': true, 'shadow': true, 'dark:bg-gray-700': true, 'dark:divide-gray-600': true }"
					id="user-dropdown">
					<div class="px-4 py-3">
						<span class="block text-sm text-gray-900 dark:text-white">{{ user.first_name }}</span>
						<span
							class="block text-sm  text-gray-500 truncate dark:text-gray-400">{{ user.email }}</span>
					</div>
					<ul class="py-2" aria-labelledby="user-menu-button">
						<li>
							<a href="#"
								class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Dashboard</a>
						</li>
						<li>
							<a href="#"
								class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Settings</a>
						</li>
						<li>
							<a href="#"
								class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Earnings</a>
						</li>
						<li>
							<a href="#" @click="logout"
								class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Sign
								out</a>
						</li>
					</ul>
				</div>
				<button data-collapse-toggle="navbar-user" type="button"
					class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
					aria-controls="navbar-user" aria-expanded="false">
					<span class="sr-only">Open main menu</span>
					<svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
						viewBox="0 0 17 14">
						<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
							d="M1 1h15M1 7h15M1 13h15" />
					</svg>
				</button>
			</div>

			<div v-else class="mx-auto items-center justify-between w-full md:flex md:w-auto" id="navbar-user">
				<ul
					class="flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg md:space-x-10 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 bg-bgGrey">
					<li>
						<a :href="loginUrl"
							class="block py-2 px-3 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 md:dark:text-blue-500"
							aria-current="page">Login</a>
					</li>
					<li>
						<a :href="registerUrl"
							class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Register</a>
					</li>
				</ul>
			</div>

		</div>
	</nav>
</template>


<script setup lang="ts">
import { ref, onMounted } from "vue";
import veducationLogo from "../assets/VEDUCATION.png"
import profileImage from "../assets/me.jpg"
import { useRouter } from "vue-router";
import Cookies from "js-cookie";
import apiClient from "../plugins/axios";
import { computed } from "vue";

const dropDownVisible = ref(false);
const dropDownVisibleMore = ref(false);
const router = useRouter();
const user = ref(null);
const error = ref(null);
const registerUrl = computed(() => `${import.meta.env.VITE_BASE_URL}/register`);
const loginUrl = computed(() => `${import.meta.env.VITE_BASE_URL}/login`);


const toggleDropDown = (dropDownId: string) => {
	if (dropDownId === "profileMenu") {
		dropDownVisible.value = !dropDownVisible.value;
	} else if (dropDownId === "moreMenu") {
		dropDownVisibleMore.value = !dropDownVisibleMore.value;
	}
}

const fetchAuthenticatedUser =  async() => {
	try {
		const response = await apiClient.get("api/user/me");
		user.value = response.data;
	} catch (err: any) {
		error.value = err.response?.data?.detail || 'Failed to fetch user data';
	}
}

onMounted(() => {
	document.addEventListener('click', (event) => {
		const userMenuButton = document.getElementById('user-menu-button');
		const userDropDown = document.getElementById('user-dropdown');
		const subMenuButton = document.getElementById('submenu-button');
		const subMenuDropDown = document.getElementById('submenu-dropdown');

		if (userMenuButton && userDropDown && !userMenuButton.contains(event.target as Node) && !userDropDown.contains(event.target as Node)) {
			dropDownVisible.value = false;
		}
		if (subMenuButton && subMenuDropDown && !subMenuButton.contains(event.target as Node) && !subMenuDropDown.contains(event.target as Node)) {
			dropDownVisibleMore.value = false;
		}
	});

	fetchAuthenticatedUser();
});

const logout = () => {
	Cookies.remove("access_token");
	Cookies.remove("refresh_token");
	router.push({ name: "Login" });
}
</script>

