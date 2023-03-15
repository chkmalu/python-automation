import boto3
from operator import itemgetter
import schedule
import time

client = boto3.client('ec2')

def snap():
    get_snapshots = client.describe_snapshots(OwnerIds=['self'])['Snapshots']
    sort_by_date = sorted(get_snapshots, key=itemgetter('StartTime'),reverse=True)

    for snap in sort_by_date[2]:
        print(f"Removing snap id:{snap['SnapshotId']}")
        client.delete_snapshot(SnapshotId=snap['SnapshotId'],)

snap()