from elasticsearch import Elasticsearch


def get_all_indices():
    es = Elasticsearch()
    indices = es.indices.get_alias("*")
    
    res = [i for i in indices.keys() if i[0] != '.']

    return res


print(get_all_indices())
