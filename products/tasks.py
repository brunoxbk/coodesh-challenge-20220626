import os
from django.conf import settings
from desafio_byx.celery import app


@app.task
def task_one():
    print(" task one called and worker is running good")
    return "success"


@app.task
def run_crawler():
    os.system("cd /code && scrapy crawl openfood")
