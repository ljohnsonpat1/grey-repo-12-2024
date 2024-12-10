import boto3    
s3 = boto3.resource('s3')

# create a S3 bucket
s3.create_bucket(Bucket='ljnewbucket')
