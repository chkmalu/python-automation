import boto3
import botocore.exceptions
from os import environ

client = boto3.client('elbv2',
  aws_access_key_id=environ['AWS_ACCESS_KEY_ID'],
  aws_secret_access_key=environ['AWS_SECRET_ACCESS_KEY'],
  region_name=environ['AWS_REGION'],
  aws_session_token=environ['AWS_SESSION_TOKEN'])

elb = client.describe_load_balancers()
get_elb = elb['LoadBalancers']
lstn_arns = []

for lb in get_elb:
    lb_arn = (lb['LoadBalancerArn'])
    # lb_arns.append(lb['LoadBalancerArn'])
    lb_name = lb['LoadBalancerName']
    
    lstn_arn = client.describe_listeners(
        LoadBalancerArn=lb_arn,
    )
    for ltn in lstn_arn['Listeners']:
        if ltn['Protocol'] == 'HTTP':
            lstn_arns.append(ltn['ListenerArn'])


for arn in lstn_arns:
    try:
        response = client.modify_listener(
            ListenerArn=arn,
            # SslPolicy='ELBSecurityPolicy-FS-1-2-Res-2020-10'
        )
        print(f'{arn} LISTENER MODIFIED')
    except botocore.exceptions.ClientError:
        print('A certificate must be specified for HTTPS listeners')