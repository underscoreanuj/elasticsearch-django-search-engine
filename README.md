# elasticsearch-django-search-engine
a simple search engine built using django and elasticserach


# How to run

1. install all required libraries using pip
`pip install -r requirements.txt`

2. make sure an elasticsearch instance is running at localhost:9200 (if you're using some other address and\or port make sure you do the changes in the code)

3. run index_data.py

4. now go inside the es_search_engine and start the django server `python manage.py runserver`

5. Now, you can go to : `http://localhost:8000/home` to see a list of available indices in elasticsearch.

6. Click on flipkart_dataset and you can search data in the search page that follows.
