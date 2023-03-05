import boto3

get_client = boto3.client('ec2')
get_vpc = get_client.describe_vpcs()['Vpcs']

create_resource = boto3.resource('ec2')
vpc = create_resource.create_vpc(CidrBlock='10.0.0.0/16')
vpc_tag = vpc.create_tags(Tags=[{'Key': 'Name','Value': 'Dev_vpc'},])
subnet = vpc.create_subnet(CidrBlock='10.0.1.0/24')
subnet = vpc.create_subnet(CidrBlock='10.0.2.0/24')
vpc_tag = subnet.create_tags(Tags=[{'Key': 'Name','Value': 'Dev_subnet'},])

for vpc in get_vpc:
    print(f"cidr_blk : {vpc['CidrBlock']}")