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


def index_sample_documents():
    sample_data =[
        {
            'name': 'Product A',
            'category': 'Electronics',
            'timestamp': '2023-01-01T10:00:00Z',
            'price': 99.99,
            'rating': 4.5,
        },
        {
            'name': 'Product B',
            'category': 'Electronics',
            'timestamp': '2023-01-02T12:00:00Z',
            'price': 149.99,
            'rating': 4.2,
        },
        {
            'name': 'Product C',
            'category': 'Clothing',
            'timestamp': '2023-01-03T14:00:00Z',
            'price': 29.99,
            'rating': 4.8,
        },
        {
            'name': 'Product D',
            'category': 'Clothing',
            'timestamp': '2023-01-04T09:30:00Z',
            'price': 39.99,
            'rating': 4.6,
        },
        {
            'name': 'Product E',
            'category': 'Furniture',
            'timestamp': '2023-01-05T16:45:00Z',
            'price': 499.99,
            'rating': 4.2,
        },
        {
            'name': 'Product F',
            'category': 'Furniture',
            'timestamp': '2023-01-06T11:15:00Z',
            'price': 799.99,
            'rating': 4.7,
        },
        {
            'name': 'Product G',
            'category': 'Electronics',
            'timestamp': '2023-01-07T09:20:00Z',
            'price': 79.99,
            'rating': 4.4,
        },
        {
            'name': 'Product H',
            'category': 'Clothing',
            'timestamp': '2023-01-08T15:30:00Z',
            'price': 59.99,
            'rating': 4.9,
        },
        {
            'name': 'Product I',
            'category': 'Furniture',
            'timestamp': '2023-01-09T13:00:00Z',
            'price': 199.99,
            'rating': 4.3,
        },
        {
            'name': 'Product J',
            'category': 'Clothing',
            'timestamp': '2023-01-10T14:30:00Z',
            'price': 19.99,
            'rating': 4.2,
        },
    ]

    for i,doc in enumerate(sample_data):
        response = client.index(index='products01',id= i+1,document=doc)
        print(f'Indexed document {i+1}: {response}')


# index_sample_documents()


terms_aggregations ={
    "category_terms":{
        "terms":{
            "field":"category.keyword"
        }
    }
}

# result = client.search(index="products01",aggs=terms_aggregations)
#
# for bucket in result["aggregations"]["category_terms"]["buckets"]:
#     print(f"category:{bucket['key']},Count: {bucket['doc_count']}")


date_histogram_aggregations = {
    "daily_product_count":{
        "date_histogram":{
            "field": "timestamp",
            "calendar_interval":"1M"
        }
    }
}


# result = client.search(index="products01",aggs=date_histogram_aggregations)
#
# for bucket in result["aggregations"]["daily_product_count"]["buckets"]:
#     print(f"Date: {bucket['key_as_string']}, Count: {bucket['doc_count']}")


range_aggregations ={
    "price_ranges":{
        "range":{
            "field":"price",
            "ranges":[
                {"from":0,"to":100},
                {"from":100,"to":500},
                {"from":500,"to":1000},
            ]
        }
    }
}

# result = client.search(index="products01", aggs=range_aggregations)
#
# for bucket in result["aggregations"]["price_ranges"]["buckets"]:
#     print(f"Price range: {bucket['key']},Count: {bucket['doc_count']}")


metrics_aggregations ={
    "averge_rating":{
        "min":{
            "field":"rating"
        }
    }
}

result = client.search(index="products01",aggs=metrics_aggregations)

average_rating = result["aggregations"]["averge_rating"]["value"]
print(f"average rating: {average_rating}")










