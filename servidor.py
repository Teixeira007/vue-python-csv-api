from flask import Flask, render_template, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

df = pd.read_csv("Relatorio_cadop.csv", delimiter=';')


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    result = df[df['Razao_Social'].str.contains(query, case=False)]

    result = result.where(pd.notna(result), None)
    
    result_json = result.to_dict(orient='records')
    result_json = result.to_json(orient='records', date_format='iso', default_handler=str)

    return result_json

if __name__ == '__main__':
    app.run(debug=True)