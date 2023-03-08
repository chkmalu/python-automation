import boto3

client = boto3.client('ec2')

devices = client.describe_instances()['Reservations']
def create_tag(res_id,kn,vn):
    tag_name = client.create_tags( Resources=[res_id,
        ],
        Tags=[
            {
                'Key': kn,
                'Value': vn
            }])

for device in devices:
    instance = (device['Instances'])
    for int in instance:
        get_volid = (int['BlockDeviceMappings'])
        for id in get_volid:
            vol_id = (id['Ebs']['VolumeId'])
    for inst in instance:
        value = inst['Tags']
        for val in value:
            val_name = (val['Value'])
            key_name = 'Name'
    create_tag(vol_id,key_name,val_name)