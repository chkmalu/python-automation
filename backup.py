import boto3
import schedule
import time

client = boto3.client('ec2')

#filter for a single volume, remove the filter to capture all volumes
get_vol = client.describe_volumes(Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['Nexus-server',]
        },
    ],)['Volumes']

def backup():
    for vol in get_vol:
        vol_tag = (vol['Tags'])
        #get the volume the tag to tag th snapshot
        for tag in vol_tag:
            name = tag['Key']
            value = tag['Value']
        vol_id = vol['Attachments']
        #get the volume id to create snapshot
        for id in vol_id:
            snap = client.create_snapshot(VolumeId=id['VolumeId'],TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {
                        'Key': name,
                        'Value': value
                    },
                ]
            },
        ])
            print(f"{value} snapshot created")


schedule.every().saturday.at("12:00").do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)