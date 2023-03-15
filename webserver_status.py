import requests
import boto3
import time
import schedule

client = boto3.client('ec2')
url = 'https://www.accelerexnetwork.com/'
get_status = requests.get(url).status_code
int_id = 'i-09f0791ae4b703c80'


def stop_instance():
    print('stopping server')
    stop_int = client.stop_instances(InstanceIds=[int_id,])
    time.sleep(5)

def start_instance():
    int_status = client.describe_instance_status(InstanceIds=[int_id,],IncludeAllInstances=True)
    for status in int_status['InstanceStatuses']:
        if status['InstanceState']['Name'] == 'pending' or status['InstanceState']['Name'] == 'running' or status['InstanceState']['Name'] == 'stopping':
            continue
        elif status['InstanceState']['Name'] == 'stopped':
            print('instance is stopped, starting instance')
            start_int = client.start_instances(InstanceIds=[int_id,])
            time.sleep(5)

#main task
def check_status():
    get_status = requests.get(url).status_code
    if get_status == 200:
        print(f"application is up and running with status code: {get_status}")
        print('#'*150)
    else:
        print(f"application is down with error code {get_status}")
        stop_instance()
        start_instance()


schedule.every(10).seconds.do(check_status)

while True:
    schedule.run_pending()
    time.sleep(1)