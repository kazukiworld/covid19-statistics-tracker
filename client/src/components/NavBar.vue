<template>
    <!-- Header navigation bar -->
    <nav
        class="z-20 w-full bg-[#1D425E] fixed top-0 px-2 md:px-12 lg:px-48 lg:space-x-10 lg:flex lg:justify-between lg:items-center">
        <div class="h-16 flex items-center justify-between">
            <!-- Title of the application -->
            <h1 class="text-xl font-bold text-gray-100 md:text-2xl">
                COVID-19 Statistics
            </h1>

            <!-- Toggle navigation button for mobile view -->
            <div v-on:click="toggleNavigationVisibility" class="flex lg:hidden">
                <button type="button" class="text-gray-100 hover:text-gray-400 focus:outline-none focus:text-gray-400">
                    <!-- Show close icon if the menu is visible, else show menu icon -->
                    <CloseIcon v-if="isNavigationVisible" class="w-6 h-6 fill-white" />
                    <MenuIcon v-else class="w-6 h-6 fill-white" />
                </button>
            </div>
        </div>

        <!-- Navigation links -->
        <div :class="isNavigationVisible ? 'flex' : 'hidden'"
            class="flex flex-col pb-4 space-y-4 text-slate-300 lg:flex lg:space-y-0 lg:flex-row lg:items-center lg:pb-0 lg:space-x-10">
            <router-link name="Home" to="/home" v-on:click="toggleNavigationVisibility">Home</router-link>
            <router-link name="Statistics" to="/statistics" v-on:click="toggleNavigationVisibility">Statistics</router-link>
            <router-link name="Contact" to="/contact" v-on:click="toggleNavigationVisibility">Contact</router-link>
        </div>
    </nav>
    <!-- Filler div for spacing -->
    <div class="h-16" />
</template>

<script setup lang="ts">
import { ref } from 'vue';
import MenuIcon from './icons/MenuIcon.vue';
import CloseIcon from './icons/CloseIcon.vue'

// Reactive variable to hold navigation visibility state
const isNavigationVisible = ref(false);

// Function to toggle navigation visibility
const toggleNavigationVisibility = () => (isNavigationVisible.value = !isNavigationVisible.value);
</script>