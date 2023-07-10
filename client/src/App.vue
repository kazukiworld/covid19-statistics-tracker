<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
</script>

<template>
  <header>
    <!-- Navigation bar -->
    <NavBar />
  </header>
  <!-- Router that holds all the pages -->
  <RouterView />
</template>
