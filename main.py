from elasticsearch import Elasticsearch
from elasticsearch.exceptions import RequestError
from elasticsearch.helpers import bulk

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


def create_document(index, id, documnet):
    try:
        resp = client.index(index=index, id=id, document=documnet)
        return resp
    except RequestError as e:
        print(f"Error while indexing document: {e}")


document = {
    'title': 'Introduction to elasticsearch',
    'description': 'Learn the basics of elasticsearch and python'
}


# response = create_document(index='index001',id=2,documnet=document)
# print(response)

def update_document(index, id, update_doc):
    try:
        res = client.update(index=index, id=id, doc=update_doc)
        return res
    except RequestError as e:
        print(f"Error while updating document: {e}")


updated_doc = {
    'description': 'Master elasticsearch and python integration'
}


# response = update_document(index='index001',id=2,update_doc=updated_doc)
# print(response)

def delete_document(index, id):
    try:
        res = client.delete(index=index, id=id)
        return res
    except RequestError as e:
        print(f"Error while deleting document: {e}")


# response = delete_document(index='index001', id=2)
# print(response)


documents =[
    {
        '_op_type': 'index',
        '_index': 'products',
        '_source':{
            'name':'product 1',
            'price':100.00,
            'category': 'books',
            'description': 'A good book'
        }
    },
{
        '_op_type': 'index',
        '_index': 'products',
        '_source':{
            'name':'product 2',
            'price':150.00,
            'category': 'books',
            'description': 'A good book'
        }
    }
]

success, failed = bulk(client, documents, index='products')

print(f'Successfully indexed {success} documents')
print(f'Failed to index {len(failed)} documents')
print(f'Errors {failed} documents')