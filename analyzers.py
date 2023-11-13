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
        "description":{
            "type":"text",
            "analyzer":"custom_analyzer"
        }
    }
}

settings={
    "analysis":{
        "char_filter":{
            "html_strip":{
                "type":"html_strip"
            }
        },
        "tokenizer":{
            "standard_tokenizer":{
                "type":"standard"
            }
        },
        "filter":{
            "lowercase_filter":{
                "type":"lowercase"
            },
            "english_stop_filter":{
                "type":"stop",
                "stopwords":"_english_"
            }
        },
        "analyzer":{
            "custom_analyzer":{
                "type":"custom",
                "char_filter":["html_strip"],
                "tokenizer":"standard_tokenizer",
                "filter":["lowercase_filter","english_stop_filter"]
            }
        }
    }
}

# result = client.indices.create(index="products02",mappings=mappings,settings=settings)
# print(result)

product_document ={
    "description":"This is a high quality product. Its perfect for tech needs"
}

# response = client.index(index="products02",document=product_document)
# print(response)

query = {
    "match":{
        "description":"tech"
    }
}

result = client.search(index="products02",query=query)
print(result)