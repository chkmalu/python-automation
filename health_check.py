import boto3
import schedule
import time

client = boto3.client('ec2')

def get_status():
    int_status = client.describe_instance_status(InstanceIds=['i-0a9c4701123237b9e',],IncludeAllInstances=True)
    print('#'*150)
    for status in int_status['InstanceStatuses']:
        print(f"instance with id: {status['InstanceId']} \
        current state: {status['InstanceState']['Name']} \
        instance-status: {status['InstanceStatus']['Status']} \
        system-status {status['SystemStatus']['Status']}")
        if status['InstanceState']['Name'] == 'pending' or status['InstanceState']['Name'] == 'running' or status['InstanceState']['Name'] == 'stopping':
            continue
        elif status['InstanceState']['Name'] == 'stopped':
            print('instance is stopped, starting instance')
            start_int = client.start_instances(InstanceIds=['i-0a9c4701123237b9e',])
            time.sleep(5)
        elif status['InstanceStatus']['Status'] and status['SystemStatus']['Status'] != 'ok':
            print('shutting instance down')
            stop_int = client.stop_instances(InstanceIds=['i-0a9c4701123237b9e',])
            time.sleep(5)
            print('starting instance')
            start_int = client.start_instances(InstanceIds=['i-0a9c4701123237b9e',])
            time.sleep(5)
        else:
            continue

schedule.every(10).seconds.do(get_status)

while True:
    schedule.run_pending()
    time.sleep(1)