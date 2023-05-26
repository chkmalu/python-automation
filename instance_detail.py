import boto3
import time
import pandas as pd

client = boto3.client('ec2')


ec2_instance = client.describe_instances(Filters=[{'Name': 'instance-state-name','Values': ['running',]},],)['Reservations']

ec2_id = []
ec2_name = []
ec2_type = []
ec2_plaform = []

instance_details = {
    'ID' : ec2_id,
    'NAME' : ec2_name,
    'TYPE' : ec2_type,
    'PLAFORM' : ec2_plaform  
}

for ec2 in ec2_instance:
    for ec2_detail in ec2['Instances']:
        ec2_id.append(ec2_detail['InstanceId'])
        ec2_type.append(ec2_detail['InstanceType'])
        try:
            ec2_name.append(ec2_detail['Tags'][0]['Value'])
        except KeyError:
            ec2_name.append('Null')
            print(f"KeyError Occured, Instance: {ec2_detail['InstanceId']} not Taged ")
        ec2_plaform.append(ec2_detail['PlatformDetails'])

df = pd.DataFrame.from_dict(instance_details, orient='index')
df = df.transpose()
df.to_csv('instance_details.csv')
print(df)