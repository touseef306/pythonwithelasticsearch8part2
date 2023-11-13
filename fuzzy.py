from elasticsearch import Elasticsearch

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


product ={
    "name":"product ABCD"
}

# result = client.index(index="products03",document=product)
# print(result)


query ={
    "fuzzy":{
        "name":{
            "value":"pRduct",
            "fuzziness":2
        }
    }
}

query1 ={
    "match":{
        "name":"poduct"
    }
}

response = client.search(index="products03",query=query1)
print(response)