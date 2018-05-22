print("https://tryolabs.com/blog/2015/02/17/python-elasticsearch-first-steps/")
# Elastic Search Synonyms, best tutorial found so far:
print("https://medium.com/@lucasmagnum/elasticsearch-setting-up-a-synonyms-search-facea907ef92")

import requests
from elasticsearch import Elasticsearch
import json

# res = requests.get('http://elasticsearch_kss:9200')
# print(res.content.decode('utf-8'))

es = Elasticsearch([{
    'host': 'elasticsearch_kss',
    'port': 9200,
}])

# print(es_sets)

def create_index():

    import os
    path = os.path.realpath(__file__)
    curdir = path[:-len(os.path.basename(path))]
    es_sets = open(curdir + 'setts.json').read()
    body = es_sets # TODO THIS IS NOT working as expected, it is not filled in
    es.create(index='sw', body=body, doc_type='mydoc')
    print("CREATED")

# create_index()
# Manually
# Update Index Settings:
# curl -X POST 'http://elasticsearch_kss:9200/laptops/_close'
# curl -X PUT 'http://elasticsearch_kss:9200/laptops/_settings' -d '{"settings":{"index":{"analysis":{"analyzer":{"synonym_analyzer":{"tokenizer":"whitespace","filter":["synonym_filter"]}},"filter":{"synonym_filter":{"type":"synonym","ignore_case":true,"expand":true,"synonyms":["Leia, Darth"]}}}}},"mappings":{"_default_":{"dynamic_templates":[{"string_fields":{"match":"*","match_mapping_type":"string","mapping":{"type":"string","analyzer":"synonym_analyzer"}}}]}}}'
# curl -X POST 'http://elasticsearch_kss:9200/laptops/_open'

# Then read the updated analyzer settings
# curl -X GET 'http://elasticsearch_kss:9200/sw/_settings?pretty'

# change_settings()

def fill_data():
    ii = 1
    while True:
        r = requests.get('http://swapi.co/api/people/' + str(ii))
        es.index(index='sw',  # sw, boogie
                 doc_type='mydoc',  # people, aliens
                 id=ii,
                 body=json.loads(r.content.decode('utf-8')))
        # obj = json.loads(r.content.decode('utf-8'))
        # print(obj)
        ii = ii + 1
        if r.status_code != 200 or ii > 10:
            break

    print("FILLED")
# fill_data()

def get_data():
    # 4: Darth Vader
    # 5: Leia Organa
    # obj = es.get(index='sw', doc_type='people', id=5)
    obj = es.get(index='starwars', doc_type='stars', id=4)
    # obj = es.get(index='boogie', doc_type='aliens', id=19)
    return json.dumps(obj, indent=True)


# print(get_data())

def search_data():
    index = "laptops"
    print(index.upper())
    obj = es.search(index=index, body={"query":
                                           {"match":
                                                {'title':
                                                     'laptop'
                                                 }
                                            }
                                       })
    return json.dumps(obj, indent=True)


print(search_data())
