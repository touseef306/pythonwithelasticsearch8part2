from elasticsearch import Elasticsearch
from flask import Flask, request, jsonify
from datetime import datetime

ELASTIC_PASSWORD = "*NsOz1wOidJ4-gTQdJE6"

client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", ELASTIC_PASSWORD),
    ca_certs="D:\\certs\\http_ca.crt"
)

if client.ping():
    print("Connected with Elasticsearch")
else:
    print("Connection Failed")

app = Flask(__name__)

index = "products07"


@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    data['timestamp'] = datetime.now()
    response = client.index(index=index, document=data)
    print(response)
    return jsonify({'message': 'product created successfully', 'result': response['result']}), 201


@app.route('/products/<string:id>', methods=['GET'])
def read_product(id):
    try:
        response = client.get(index=index, id=id)

        if response['found']:
            return jsonify(response['_source']), 200
        else:
            return jsonify({'message': 'product not found'}), 404

    except Exception as e:
        print(f"Internal Server Error:{e}")
        return jsonify({'message': 'product not found'}), 404


@app.route('/products/<string:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    data['timestamp'] = datetime.now()
    response = client.update(index=index, id=id, doc=data)
    return jsonify({'message': 'product updated successfully', 'result': response['result']}), 200


@app.route('/products/<string:id>', methods=['DELETE'])
def delete_product(id):
    try:
        response = client.delete(index=index, id=id)

        return jsonify({'message': 'product deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': "product not found"}), 404


@app.route('/custom_products', methods=['POST'])
def custom_product():
    query = request.get_json()

    if query:
        response = client.search(index=index, query=query)
        products = [hit["_source"] for hit in response['hits']['hits']]
    else:
        response = client.search(index=index, query={"match_all": {}})
        products = [hit["_source"] for hit in response['hits']['hits']]

    return jsonify(products), 200


if __name__ == '__main__':
    app.run(debug=True)
