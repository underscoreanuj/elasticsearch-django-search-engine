from elasticsearch import Elasticsearch
import requests, json


"""

GET flipkart_dataset/_search?size=1000
{
  "query": {
    "query_string": {
      "analyze_wildcard": true,
      "fuzziness": 2,
      "fields": ["product_name", "description", "url", "product_url"],
      "query": "wireless headphonees"
    }
  },
  "size": 50,
  "sort": [
    
  ]
}

"""

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
}

def get_all_indices():
    es = Elasticsearch()
    indices = es.indices.get_alias("*")
    
    res = [i for i in indices.keys() if i[0] != '.']

    return res

def query_index(index_name, query, count=10):
    payload = {
        "query": {
            "query_string": {
                "analyze_wildcard": True,
                "fuzziness": 2,
                "fields": ["product_name", "description", "url", "product_url"],
                "query": str(query)
            }
        },
        "size": 50,
        "sort": []
    }

    payload = json.dumps(payload)
    url = "http://localhost:9200/" + str(index_name) + "/_search?size=" + str(count)
    response = requests.request("GET", url, data=payload, headers=headers)
    response_dict_data = json.loads(str(response.text))

    result = [{"data": res.get("_source"), "score": res.get("_score")} for res in response_dict_data.get("hits").get("hits")]

    return result


# if __name__ == '__main__':
#     print(get_all_indices())
#     print(query_index("flipkart_dataset", "wireless headphones"))
