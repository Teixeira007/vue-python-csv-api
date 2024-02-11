<template>
  <div class="search">
    <div class="input-div">
      <!-- Campo de entrada de texto vinculado a 'query' -->
      <input type="text" v-model="query">

        <!-- Botão que chama a função search -->
      <input type="submit" @click="search" :disabled="!query.trim()" value="ENVIAR">
    </div>
    <!-- Lista de resultados de pesquisa (exibida somente se houver resultados) -->
    <ul v-if="searchResults.length > 0">
      <!-- Itera sobre os resultados e exibe cada item -->
      <li v-for="item in searchResults" :key="item.Registro_ANS" class="item">
        {{ item.Razao_Social }} | {{ item.Registro_ANS }} | {{ item.Cidade }} | {{ item.UF }}
      </li>
    </ul>

  </div>
</template>

<script>
export default {
  data() {
    // Dados do componente
    return {
      query: '',             // Armazena a consulta de pesquisa
      searchResults: [],     // Armazena os resultados da pesquisa
    };
  },
  methods: {
    // Método chamado quando o botão de enviar é clicado
    search() {
      if (this.query.trim()) {
        // Faça a requisição para o servidor Flask
        fetch(`http://localhost:5000/search?q=${this.query}`)
          .then(response => response.json())
          .then(data => {
            // Atualiza os resultados da pesquisa com os dados recebidos
            this.searchResults = data;
            cy.wait(1000);
          })
          .catch(error => {
            console.error('Error fetching data:', error);
          });
      }
    }
  },
};
</script>

<style scoped>
/* Estilos para o campo de entrada de texto */
input[type="text"]{
  font-family: 'Roboto', sans-serif;
  border-radius: 1.5rem;
  width: 25rem;
  padding: 1rem;
  border: solid 0.1rem #c8a4f4;
  outline: none;
  margin-bottom: 1rem;
}

input[type="submit"]{
  border-radius: 1.5rem;
  padding: 0.4rem;
  width: 6rem;
  border: none;
  background-color: #c8a4f4;
  cursor: pointer;
  height: 2.7rem;
  font-family: 'Roboto', sans_serif;
}

.input-div{
  display: flex;
  gap: 0.5rem;
}

input[type="submit"]:hover:enabled{
  opacity: 0.9;
  background-color: #a07fc2;
}

/* Estilos para o componente de pesquisa */
.search{
  display: flex;
  flex-direction: column;
  align-items: center;

}

/* Estilos para a lista de resultados */
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

/* Estilos para cada item na lista de resultados */
li{
  font-size:0.9rem
}
</style>
