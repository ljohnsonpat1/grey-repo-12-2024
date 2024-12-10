import boto3    
vpc = boto3.resource('ec2')

# create a new VPC
vpc = vpc.create_vpc(CidrBlock='10.0.0.0/16')
subnet = vpc.create_subnet(CidrBlock='10.0.1.0/24')
vpc.wait_until_available(
    Filters=[{
        'Name': 'state',
        'Values': ['available']
    }]
)