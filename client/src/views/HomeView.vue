<template>
  <main class="flex flex-col justify-center items-center p-8 space-y-8 lg:min-h-screen lg:h-auto lg:-mt-16">
    
    <!-- Background image of a world map, fixed and covering the full screen -->
    <img class="fixed inset-0 -z-10 object-cover w-screen h-screen" src="../assets/world-map.svg" alt="world map">
    
    <!-- Title, subtitle, and 'Get Started' button -->
    <div class="max-w-3xl flex flex-col justify-center items-center space-y-4 md:space-y-8 text-center">
      <h1 class="text-3xl md:text-6xl font-bold">
        Global Covid-19 Statistics at Your Fingertip.
      </h1>
      <h2 class="md:text-lg">
        Stay informed with real-time updates on the latest statistics regarding cases of
        COVID-19 worldwide.
      </h2>
      <router-link to="/statistics" class="px-3 py-4 bg-[#132D40] font-bold rounded text-white">
        Get Started
      </router-link>
    </div>
    
    <!-- A grid list of the key features of the application -->
    <ul class="grid md:grid-cols-3 gap-4 max-w-5xl">
      <li v-for="feature in features" :key="feature.text"
        class="flex justify-center items-center bg-white rounded border-2 p-4 space-x-2">

        <!-- Using dynamic component to render the appropriate icon for each feature -->
        <component :is="feature.icon" class="w-1/4 h-auto" />
        
        <!-- Description of the feature -->
        <p class="w-3/4">
          {{ feature.text }}
        </p>
      </li>
    </ul>
  </main>
</template>

<script setup lang="ts">
import type {Component} from 'vue';
import DropDownIcon from '@/components/icons/DropDownIcon.vue';
import TableIcon from '@/components/icons/TableIcon.vue';
import EarthIcon from '@/components/icons/EarthIcon.vue';

interface Feature {
  icon: Component;
  text: string;
}

// Define a list of features with the icon and description for each feature
const features: Feature[] = [
  { icon: DropDownIcon, text: "A dropdown menu to select a specific country or global covid-19 statistics." },
  { icon: TableIcon, text: "A table that displays key statistics like confirmed cases, recoveries, and more." },
  { icon: EarthIcon, text: "A comprehensive world map for better visualization of data." },
];
</script>