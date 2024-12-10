import boto3
security_group = boto3.resource('ec2')

# create a new security group
security_group = security_group.create_security_group(
    GroupName='lj1_security_group',
    Description='Allow SSH and HTTP access',
    VpcId='vpc-0e4e9b2e3e8e3d2f5'
)

ingress = security_group.authorize_ingress(
    GroupName='lj1_security_group',
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        },
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
    ]
)

   

