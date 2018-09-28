# simple_crawler

file that contains crawler code play_market/crawler.py 

crawling scheduled to be performed once a day

to force sart crawling use force_crawl api endpoint (below)

BUILD:
docker-compose up

API DESCTIPTION

localhost:8000/play_market/api/category/     list of all categories in db

localhost:8000/play_market/api/app/          list of all apps in db

localhost:8000/play_market/api/force_crawl/  force_start scrapping

requerements:

django==2.1.1

djangorestframework==3.8.2  togather with django used for data representation

urllib3                     used to retrieve html content from google play

psycopg2                    used to write data to Postgres

celery==4.2.1               used to schedule periodic crawl job

redis==2.10.6               used as message brocker for celery

bs4                         used to parse html content
