import boto3
import schedule
import time

client = boto3.client('ec2')

def get_status():
    int_status = client.describe_instance_status(IncludeAllInstances=True)
    print('#'*100)
    for status in int_status['InstanceStatuses']:
        print(f"instance with id: {status['InstanceId']} \
        current state: {status['InstanceState']['Name']} \
        instance-status: {status['InstanceStatus']['Status']} \
        system-status {status['SystemStatus']['Status']}")

schedule.every(5).seconds.do(get_status)

while True:
    schedule.run_pending()
    # time.sleep(1)