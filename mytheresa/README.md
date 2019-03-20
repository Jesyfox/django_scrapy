install:

1: make venv

2: create db on postgres shell


RUN:

1: open 3 terminals

2: on first type: `celery -A mytheresa_dj worker -l info`

3: on second type: `scrapy crawl boys_catalog`

4: on third type: `./manage.py runserver`
