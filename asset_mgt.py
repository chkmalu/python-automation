import pandas as pd
import boto3
from os import environ

def client_fxn(srv):
    return boto3.client(srv,
      aws_access_key_id=environ['AWS_ACCESS_KEY_ID'],
      aws_secret_access_key=environ['AWS_SECRET_ACCESS_KEY'],
      region_name=environ['AWS_REGION'],
      aws_session_token=environ['AWS_SESSION_TOKEN']
      )

get_rds = client_fxn('rds').describe_db_clusters()
get_ecs_arn = client_fxn('ecs').list_clusters()
get_elc = client_fxn('elasticache').describe_cache_clusters()
get_elb = client_fxn('elbv2').describe_load_balancers()
get_ec2 = client_fxn('ec2').describe_instances(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
    ],)


rds = []
ec2 = []
ecs = []
elc = []
elb = []

assets = {
    'RDS': rds,
    'EC2': ec2,
    'ECS': ecs,
    'ElastiCache': elc,
    'ELB': elb
}

for rd in get_rds['DBClusters']:
    rds.append(rd['Endpoint'])

for instn in get_ec2['Reservations']:
    instance = (instn['Instances'])
    for id in instance:
        ec2.append(id['InstanceId'])

for arn in get_ecs_arn['clusterArns']:
    get_ecs = client_fxn('ecs').describe_clusters(clusters=[arn])
    for clst_name  in get_ecs['clusters']:
        ecs.append(clst_name['clusterName'])

for cache in get_elc['CacheClusters']:
    elc.append(cache['CacheClusterId'])

for lb in get_elb['LoadBalancers']:
    elb.append(lb['LoadBalancerName'])

df = pd.DataFrame.from_dict(assets, orient='index')
df = df.transpose()
df.to_csv('Approve AWS Assests.csv')
print(df)