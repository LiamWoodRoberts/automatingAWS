import boto3

session = boto3.Session(profile_name="Liam")
s3 = session.resource("s3")

for bucket in s3.buckets.all():
    print(bucket)
