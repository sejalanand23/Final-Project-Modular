from sympy import re
from application.workers import celery
from datetime import datetime
import csv
import time
from flask_sse import sse

# @celery.on_after_configure.connect
# def setup_periodic_tasks(sender,**kwargs):
#     sender.add_periodic_task(10.0,daily_reminder.s(),name="After every 10 sec")

# @celery.task()
# def daily_reminder(name='daily_reminder'):
#     get_users_to_remind()
#     return ''
    

@celery.task()
def generate_csv(input):
    # sse.publish({'message':'Export Initiated'},type='export')
    with open('/Users/sejalanand/Downloads/export_information.csv', 'w', encoding='utf8', newline='') as output_file:
        output = csv.DictWriter(output_file, 
                            fieldnames=input[0].keys(),
                            restval=''
                        )
        output.writeheader()
        output.writerows(input)
    # sse.publish({'message':'Export Complete'},type='export')
    return "CSV Generated"


