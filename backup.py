import boto3

client = boto3.client('ec2')

get_vol = client.describe_volumes(Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['Nexus-server',]
        },
    ],)['Volumes']



for vol in get_vol:
    vol_tag = (vol['Tags'])
    for tag in vol_tag:
        name = tag['Key']
        value = tag['Value']
    vol_id = vol['Attachments']
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
        print(snap)