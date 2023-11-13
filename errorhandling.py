from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError, TransportError

ELASTIC_PASSWORD = "*NsOz1wOidJ4-gTQdJE6"

client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", ELASTIC_PASSWORD),
    ca_certs="D:\\certs\\http_ca.crt"
)

# connection error
# indexing error
# query error
# mapping error

try:
    if not client.ping():
        raise ConnectionError("Failed to connect with elasticsearch")

    client.index(index="products04",document={"name":"product xyz"})

    client.search(index="different_index")

except ConnectionError as ce:
    print(f"Connection error: {ce}")

except TransportError as te:
    print(f"Transport error: {te}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print("Elasticsearch operations completed successfully")

finally:
    client.close()

