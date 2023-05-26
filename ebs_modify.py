import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

def modify_ebs(vol_id, vol_type):
    vol_modify = ec2.modify_volume(VolumeId=vol_id,VolumeType=vol_type)
    return vol_modify


for reserve in response['Reservations']:
    for instance in reserve['Instances']:
        instance_id = instance['InstanceId']
        if instance.get('Platform') == 'windows':
            for ebs in instance['BlockDeviceMappings']:
                vol_id = ebs['Ebs']['VolumeId']
                ebs_modify = ec2.modify_volume(VolumeId=vol_id,VolumeType='gp3')
                modify_ebs(vol_id, 'gp3')