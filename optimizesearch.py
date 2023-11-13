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

# 1st use the track_total_hits

res = client.search(index="example_index",query={
    "match_all":{}
},track_total_hits=False)

# 2nd use source filtering

res = client.search(index="example_index",query={
    "match_all":{}
},_source=["field1","field2"])

# 3rd use the pagination wisely

res = client.search(index="example_index",query={
    "match_all":{}
},scroll="1m")

scroll_id = res['_scroll_id']

res2 = client.scroll(scroll_id=scroll_id,scroll="1m")

# 4th technique optimize indices