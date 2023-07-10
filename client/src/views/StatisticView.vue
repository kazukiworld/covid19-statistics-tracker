<template>
    <main class="p-4 flex flex-col items-center justify-center lg:min-h-screen lg:h-auto lg:-mt-16">

        <!-- If the data is still fetching, display a loading icon -->
        <div v-if="isLoading" class="w-full h-screen flex justify-center items-center -mt-16">
            <LoadingIcon />
        </div>

        <!-- If the data fetching is completed, display the data -->
        <div v-else-if="covidData"
            class="w-full max-w-7xl flex flex-col lg:flex-row justify-center items-center space-y-4 lg:space-y-0 transition-all opacity-100 z-10">

            <!-- A table with the fetched COVID-19 Data -->
            <table class="w-full lg:w-1/3 flex flex-col p-8 space-y-4 border-2 border-gray-50 rounded-lg shadow">
                <thead class="space-y-4">

                    <!-- Dropdown to select a country for which the covid stats should be displayed -->
                    <select v-model="selectedOption" class="w-full px-4 py-3 border border-gray-200">
                        <option v-for="country in countries" :key="country" :value="country">
                            {{ country }}
                        </option>
                    </select>

                    <!-- Displaying the selected country name -->
                    <h1 class="text-xl font-bold text-center">COVID-19 Statistics: {{ countryData?.["Country_text"] }}</h1>

                    <!-- Displaying the last updated time for the data -->
                    <h2 class="text-sm text-center">Last Updated: {{ countryData?.["Last Update"] }}</h2>
                </thead>

                <tbody class="flex flex-col justify-center space-y-4">
                    <!-- Looping over the stats to create a row for each stat -->
                    <tr v-for="stat in stats" :key="stat.key">
                        <th class="font-bold">{{ stat.title }}:</th>
                        <td>{{ countryData?.[stat.key] }}</td>
                    </tr>
                </tbody>
            </table>

            <!-- A map component that highlights the selected country -->
            <WorldMap class="lg:w-2/3" :selectedCountry="selectedOption" />
        </div>

        <!-- If the data fetching fails, display an error message -->
        <div v-else class="absolute w-full flex justify-center items-center">
            <div class="max-w-xl p-4 space-y-4 text-center">
                <h1 class="font-bold text-3xl">
                    Sorry! We couldn't get your statistics.
                </h1>
                <p>
                    Please try refreshing the page. If that does not work, please
                    <router-link to="/contact" class="text-blue-700 underline">
                        contact us
                    </router-link>
                    about the issue and we will get back to you promptly. We truly appreciate your patience.
                </p>
            </div>
        </div>
    </main>
</template>

<script setup lang="ts">
import { ref, onMounted, watchEffect, computed } from 'vue';
import WorldMap from '@/components/WorldMap.vue';
import LoadingIcon from '@/components/icons/LoadingIcon.vue';

// Defining CovidData and Stat types
type CovidData = {
    "Active Cases_text": string;
    "Country_text": string;
    "Last Update": string;
    "New Cases_text": string;
    "New Deaths_text": string;
    "Total Cases_text": string;
    "Total Deaths_text": string;
    "Total Recovered_text": string;
    [key: string]: string;
};

type Stat = {
    title: string;
    key: keyof CovidData;
};

// Defining reactive variables using ref
const covidData = ref<CovidData[] | null>(null);
const countryData = ref<CovidData | null>(null);
const isLoading = ref<boolean>(true);
const selectedOption = ref<string>('World');
const countries = ref<string[] | null>([]);

// Creating titles based on covid data
const stats = computed<Stat[]>(() => [
    { title: "Total Cases", key: "Total Cases_text" },
    { title: "Active Cases", key: "Active Cases_text" },
    { title: "New Cases", key: "New Cases_text" },
    { title: "Total Deaths", key: "Total Deaths_text" },
    { title: "New Deaths", key: "New Deaths_text" },
    { title: "Recovered", key: "Total Recovered_text" }
]);

// Watching for changes in the selected country to update COVID-19 data for the specific countries
watchEffect(() => {

    if (covidData.value) {
        // Find a specific data that matches the country selected from the dropdown menu
        const data = covidData.value.find(obj => obj['Country_text'] === selectedOption.value);
        countryData.value = data ? { ...data } : null;

        // If there are any blank values within the data of a specific country, output 'N/A'
        if (countryData.value) {
            for (const key in countryData.value) {
                const typedKey: string = key;
                if (countryData.value[typedKey] === '') {
                    countryData.value[typedKey] = 'N/A';
                }
            }
        }
    }
});

// Fetching covid data when the component mounts
onMounted(
    async () => {
        // Starting loading state
        isLoading.value = true;

        // Defining API url
        const apiUrl: string = import.meta.env.VITE_APP_API_BASE_URL;

        try {
            // Fetching covid data from the API
            const response = await fetch(`${apiUrl}/api/covid-statistics`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            // Storing the fetched covid data in covidData ref
            covidData.value = await response.json();

            // Sorting the list of countries from the fetched data in alphabetical order
            countries.value = covidData.value?.map((data: CovidData) => data.Country_text).sort() || null;

            // Adding 'World' option at the beginning of the countries list
            countries.value?.unshift("World");

        } catch (error: any) {

            // Logging any error that occurs during the fetch operation
            console.error('There has been a problem with your fetch operation:', error);
        } finally {

            // Ending loading state
            isLoading.value = false;
        }
    }
);
</script>