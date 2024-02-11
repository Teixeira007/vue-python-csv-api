from flask import Flask, request
import pandas as pd
from flask_cors import CORS

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Configuração para permitir solicitações de origens diferentes
CORS(app)

# Lê um arquivo CSV chamado "Relatorio_cadop.csv" e carrega os dados em um DataFrame do Pandas
df = pd.read_csv("Relatorio_cadop.csv", delimiter=';')

# Define uma rota para a pesquisa, usando o método HTTP GET
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

# Inicia o aplicativo Flask quando o script é executado diretamente, com a opção de depuração habilitada
if __name__ == '__main__':
    app.run(debug=True)