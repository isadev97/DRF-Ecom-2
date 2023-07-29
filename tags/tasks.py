
from celery import shared_task

@shared_task
def process(number):
    sm = 0 
    for i in range(1,number+1):
        sm+=i 
    return sm