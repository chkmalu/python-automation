import boto3

client = boto3.client('ec2')
ec2_rosource = boto3.resource('ec2')

int_id = 'i-0aa3bc265b59224bb'

#get the volume id to determine the snapshot associated to it
vol_id = client.describe_volumes(
    Filters=[
        {
        'Name': 'attachment.instance-id',
        'Values': [int_id,
        ]
    }])['Volumes'][0]['VolumeId']

#get the snapshot id to create new volume from the snapshot
snap_id = client.describe_snapshots(OwnerIds=['self'],Filters=[
        {
            'Name': 'volume-id',
            'Values': [
                vol_id,
            ]
        },
    ])['Snapshots'][0]['SnapshotId']


#create new volume with the snapshot id and get the volume id
create_vol = client.create_volume(
    AvailabilityZone='us-east-1a',
    SnapshotId=snap_id,
    VolumeType='gp2',
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Nexus-server'
                },
            ]
        },
    ],)['VolumeId']

#attach volume to the instance
while True:
    volume = ec2_rosource.Volume(create_vol)
    print(volume.state)
    if volume.state == 'available':
        attch_vol = volume.attach_to_instance(
            Device='/dev/sdx',
            InstanceId= int_id,
        )
        print('volume attached')
        break