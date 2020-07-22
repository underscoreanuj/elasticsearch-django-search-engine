from elasticsearch import helpers, Elasticsearch
import csv
from datetime import datetime

es = Elasticsearch()

mapping = {
  "settings": {
      "number_of_shards": 1,
    "index": {
      "max_ngram_diff": 2
    },
    "analysis": {
      "analyzer": {
        "default": {
          "tokenizer": "whitespace",
          "filter": [ "lowercase", "3_5_grams", "stemmer" ]
        }
      },
      "filter": {
        "3_5_grams": {
          "type": "ngram",
          "min_gram": 3,
          "max_gram": 5
        }
      }
    }
  }
}

response = es.indices.create(
    index="flipkart_dataset",
    body=mapping
)

print ('response:', response)

with open("./dataset/flipkart_com-ecommerce_sample.csv") as f:
    reader = csv.DictReader(f)
    res = helpers.bulk(es, reader, index='flipkart_dataset', doc_type='products')


print("done")




"""

GET flipkart_dataset/_search
{
  "query": {
    "query_string": {
      "query": "wereless",
      "default_field": "description",
      "fuzziness": 2
    }
  }
}

"""