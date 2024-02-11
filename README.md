# Sistema de Pesquisa com Vue.js e Flask API
Desenvolvimento de uma interface web com Vue.js que interage com um servidor Python para realizar buscas textuais na lista de cadastros de operadoras, utilizando dados de um CSV. Inclui uma rota no servidor para processar as consultas e uma coleção no Postman para demonstrar os resultados.

## Servidor Flask (Back-End)
Este repositório contém uma API desenvolvida em Flask, uma estrutura leve para construir aplicativos web em Python. O objetivo principal desta API é realizar pesquisas em um conjunto de dados armazenado em um arquivo CSV, utilizando a biblioteca Pandas para manipulação eficiente dos dados.

### Pré-requisitos
Antes de executar a API, certifique-se de ter o Python instalado em sua máquina. Você pode instalar as dependências usando o seguinte comando:
```bash
pip install flask pandas flask-cors
```

### Executando a API
1. Clone este repositório em sua máquina local:
 ```git
   git clone https://github.com/Teixeira007/vue-python-csv-api.git
 ```
2. Execute a API:
```bash
python servidor.py
```
A API estará disponível em http://127.0.0.1:5000/
### Uso da API
A API fornece uma rota de pesquisa em http://127.0.0.1:5000/search. Você pode realizar uma pesquisa incluindo um parâmetro 'q' na URL. Por exemplo:
```bash
http://127.0.0.1:5000/search?q=termo_de_pesquisa
```
Isso retornará os resultados da pesquisa em formato JSON, filtrando os dados do arquivo CSV com base na coluna 'Razao_Social'.

### Estrutura do Código
### Bibliotecas Utilizadas
```python
from flask import Flask, request
import pandas as pd
from flask_cors import CORS
```

#### Flask App: O código utiliza o Flask para criar uma instância da API web.
```python
app = Flask(__name__)
```

#### CORS: Configuração para permitir solicitações de origens diferentes (Cross-Origin Resource Sharing).
```pyhton
CORS(app)
```
#### Pandas DataFrame: A API lê um arquivo CSV e carrega os dados em um DataFrame do Pandas para manipulação eficiente.
```python
df = pd.read_csv("Relatorio_cadop.csv", delimiter=';')
```
### Rota de Pesquisa (/search): Uma rota que aceita solicitações GET e retorna os resultados da pesquisa em formato JSON.
```python
@app.route('/search', methods=['GET'])
def search():
    # Obtém o parâmetro 'q' da consulta da URL
    query = request.args.get('q')

    # Filtra o DataFrame para obter resultados que contenham a consulta na coluna 'Razao_Social'
    result = df[df['Razao_Social'].str.contains(query, case=False)]

    # Substitui os valores NaN (nulos) por None
    result = result.where(pd.notna(result), None)

    # Converte o DataFrame filtrado para um dicionário Python
    result_json = result.to_dict(orient='records')

    # Converte o dicionário para uma string JSON, incluindo opções de formato
    result_json = result.to_json(orient='records', date_format='iso', default_handler=str)

    # Retorna os resultados em formato JSON
    return result_json
```
## Front-End (Vue.js)
O front-end é construído utilizando Vue.js para uma interação dinâmica e responsiva com o usuário. A interface é composta por um componente de pesquisa, oferecendo uma experiência intuitiva.
### Pré-requisitos
1. Verifique se o servidor flask (back-end) já está rodando
2. Antes de executar o aplicativo, certifique-se de ter instalado:
  - Node.js: Instale o [Node.js](https://nodejs.org/en) para gerenciar as dependências do Vue.js.

### Executando o Front-End
1. Navegue até o diretório do front-end:
 ```bash
   cd front
 ```
2. Instale as dependências do Vue.js:
```bash
npm install
```
3. Execute o aplicativo Vue.js:
```bash
npm run dev
```
O Front estará disponível em http://127.0.0.1:5173/

### Estrutura do Código
#### Componente de Pesquisa
```html
<template>
  <div class="search">
    <div class="input-div">
      <input type="text" v-model="query">
      <input type="submit" @click="search" :disabled="!query.trim()" value="Pesquisar">
    </div>
    <ul v-if="searchResults.length > 0">
      <li v-for="item in searchResults" :key="item.Registro_ANS" class="item">
        {{ item.Razao_Social }} | {{ item.Registro_ANS }} | {{ item.Cidade }} | {{ item.UF }}
      </li>
    </ul>
  </div>
</template>
```
1. Campos de Entrada e Botão:
 - Um campo de entrada de texto para inserir o termo de pesquisa, vinculado ao modelo query.
 - Um botão de "Pesquisar" que aciona a função search quando clicado.
2. Lista de Resultados:
 - Exibe dinamicamente os resultados da pesquisa em uma lista.
#### Script Vue.js
```js
<script>
export default {
  data() {
    return {
      query: '',             // Armazena a consulta de pesquisa
      searchResults: [],     // Armazena os resultados da pesquisa
    };
  },
  methods: {
    search() {
      if (this.query.trim()) {
        fetch(`http://localhost:5000/search?q=${this.query}`)
          .then(response => response.json())
          .then(data => {
            this.searchResults = data;
          })
          .catch(error => {
            console.error('Erro ao buscar dados:', error);
          });
      }
    }
  },
};
</script>
```
1. Data:

- Define o estado do componente, incluindo:
  ```query``` para armazenar a consulta de pesquisa
  ```searchResults``` para armazenar os resultados.
2. Método search():

 - Chamado quando o botão é clicado.
 - Envia uma solicitação para a API Flask usando fetch com o termo de pesquisa atual.
 - Atualiza searchResults com os resultados obtidos.
## Coleção de Testes no Postman
- Nome da Coleção: Sistema de Busca
- Descrição: A coleção contém testes automatizados para verificar a resposta da API Flask ao realizar uma pesquisa.
- Testes Incluídos: Teste de Status Code 200, Verifica se o código de status da resposta é 200 (OK).

### Como Executar a Coleção no Postman:
1. Abra o Postman.

2. Importe a coleção "SistemaBusca.postman_collection" para o Postman.

3. Execute a coleção.

Certifique-se de que o servidor Flask está em execução (http://localhost:5000).

O teste automatizado irá enviar uma solicitação GET para http://localhost:5000/search?q=termo_de_pesquisa e verificará se o código de status da resposta é 200.

Caso haja falhas nos testes, revise a configuração da API ou do ambiente.

OBS: O uso do Postman para automação de testes facilita a validação da integridade e funcionalidade da API Flask. A coleção de testes proporciona uma abordagem eficaz para garantir a confiabilidade do serviço.

## Resultados
