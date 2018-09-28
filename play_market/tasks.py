from celery import shared_task
from django.core.management import call_command


@shared_task
def crawl_play_market():
    call_command('crawl_play_market')
