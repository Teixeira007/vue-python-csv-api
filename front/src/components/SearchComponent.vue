<!-- SearchComponent.vue -->

<template>
  <div class="search">
    <input type="text" v-model="query" @input="search">
    <ul v-if="searchResults.length > 0">
      <li v-for="item in searchResults" :key="item.id" class="item">
        {{ item.Razao_Social }} | {{ item.Registro_ANS }} | {{ item.Cidade }} | {{ item.UF }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: '',
      searchResults: [],
    };
  },
  methods: {
    search() {
      // Faça a requisição para o servidor Flask
      // Certifique-se de que o servidor Flask está em execução
      fetch(`http://localhost:5000/search?q=${this.query}`)
        .then(response => response.json())
        .then(data => {
          this.searchResults = data;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    }
  },
};
</script>

<style scoped>
/* c8a4f4 */
input{
  font-family: 'Roboto', sans-serif;
  border-radius: 1.5rem;
  width: 25rem;
  padding: 1rem;
  border: solid 0.1rem #c8a4f4;
  outline: none;
  margin-bottom: 1rem;
}

.search{
  display: flex;
  flex-direction: column;
  align-items: center;

}

ul{
  list-style: none;
  display: flex;
  flex-direction:column;
  gap: 0.8rem;
  justify-content: center;
  background-color: #c8a4f4;
  padding: 2rem;
  border-radius: 2rem;
}

li{
  font-size:0.9rem
}
</style>
