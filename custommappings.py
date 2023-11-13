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


mappings ={
    "properties":{
        "name":{
            "type":"text",
            "analyzer":"standard",
            "fields":{
                "keyword":{
                    "type":"keyword"
                }
            }
        },
        "category":{
            "type":"keyword"
        },
        "price":{
            "type":"double"
        },
        "description":{
            "type":"text",
            "analyzer":"english"
        },
        "timestamp":{
            "type":"date",
            "format":"yyyy-MM-dd'T'HH:mm:ss'Z'"
        }
    }
}


# response = client.indices.create(index="products",mappings=mappings)
# print(response)


product_document = {
    "name": "Product b",
    "category": "Electronics",
    "price": 199.99,
    "description": "A high-quality electronic product",
    "timestamp": "2023-01-01T10:00:00Z"
}

# resp = client.index(index="products",document=product_document)
# print(resp)

query = {
    "term": {
        "category": "Electronics"
    }
}

# result = client.search(index="products",query=query)
# print(result)


query1={
    "price":{
        "order":"desc"
    }
}


result = client.search(index="products",sort=query1)
print(result)