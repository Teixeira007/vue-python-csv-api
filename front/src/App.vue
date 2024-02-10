<script setup>
import SearchComponent from './components/SearchComponent.vue';
</script>

<template>
  <header>
    <img class="logo" src="./assets/intuitive-care_site-1.png" alt="Logo da intuitive care"/>
  </header>
  
  <main class="container">
    <SearchComponent/>
  </main>
</template>

<style scoped>
.container{
  display: flex;
  justify-content:center;
  width: 59rem;
  margin: 1rem auto;
}

.logo{
  width: 10rem;
}

header{
  margin-top: 3rem;
  display: flex;
  justify-content:center;
}
</style>
