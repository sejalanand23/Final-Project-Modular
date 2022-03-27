from application.workers import celery
from datetime import datetime
import csv
import pandas as pd
import time

@celery.task()
def hello():
    return "Hello from celery task"

@celery.task()
def generate_csv(input):
    time.sleep(15)
    with open('/Users/sejalanand/Downloads/export_information.csv', 'w', encoding='utf8', newline='') as output_file:
        output = csv.DictWriter(output_file, 
                            fieldnames=input[0].keys(),
                            restval=''
                        )
        output.writeheader()
        output.writerows(input)
    return "CSV Generated"


