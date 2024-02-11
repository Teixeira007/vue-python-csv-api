<script setup>
import SearchComponent from './components/SearchComponent.vue';
</script>

<template>
  <header>
    <!-- Logo do intuitive care -->
    <img class="logo" src="./assets/intuitive-care_site-1.png" alt="Logo da intuitive care"/>
  </header>
  
  <main class="container">
    <!-- Componente de pesquisa -->
    <SearchComponent/>
  </main>
</template>

<style scoped>
/* Estilos para o main */
.container{
  display: flex;
  justify-content:center;
  width: 59rem;
  margin: 1rem auto;
}

/* Estilos para a logo */
.logo{
  width: 10rem;
}

/* Estilos para o cabeçalho */
header{
  margin-top: 3rem;
  display: flex;
  justify-content:center;
}
</style>
