import boto3
import collections
from datetime import datetime, date, time, timedelta

region = 'eu-central-1'

def lambda_handler(event, context):
    """
    yesterday = datetime.strptime('2018-09-19 08:30:00','%Y-%m-%d %H:%M:%S')
    today = datetime.strptime('2018-09-19 00:00:00','%Y-%m-%d %H:%M:%S')
    """
    yesterday = datetime.combine(date.today()-timedelta(1),time())
    today = datetime.combine(date.today(),time())
    unix_start = datetime(1970,1,1)
    client = boto3.client('logs')
    response = client.create_export_task(
        taskName='export_logs_to_s3',
        logGroupName='log-group.eu-central-1.01.sandbox-01.flow-logs',
        fromTime=int(yesterday.timestamp() * 1000),
        to=int(today.timestamp() * 1000),
        destination='bucket-export-logs-s3',
        destinationPrefix='myapplogs'
    )
    return 'Response from export task at {} :\n{}'.format(datetime.now().isoformat(),response)
