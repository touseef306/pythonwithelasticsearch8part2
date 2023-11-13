from elasticsearch import Elasticsearch
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

index_mappings = {
    "properties": {
        "event_date": {
            "type": "date"
        },
        "location": {
            "type": "geo_point"
        }
    }
}

# res = client.indices.create(index="events",mappings=index_mappings)
# print(res)

event = {
    'name': "Music festival",
    'event_date': datetime.now(),
    'location': {
        'lat': 40.7128,
        'lon': -74.0060
    }
}

# res = client.index(index="events",document=event)
# print(res)

query = {
    "range": {
        "event_date": {
            "gte": "now-1d/d",
            "lt": "now/d"
        }
    }
}

# res = client.search(index="events",query=query)
# print(res)

query2 ={
    "bool":{
        "must":{
            "match_all":{}
        },
        "filter":{
            "geo_distance":{
                "distance":"200km",
                "location":{
                    "lat": 40.7128,
                    "lon":-74.0060
                }
            }
        }
    }
}

res = client.search(index="events",query=query2)
print(res)