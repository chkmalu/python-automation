# import boto3


# client = boto3.client(
#   'ec2'
# )

# response = client.describe_instances()
# print(response)
import boto3
sts = boto3.client('sts')
print(sts.get_caller_identity())