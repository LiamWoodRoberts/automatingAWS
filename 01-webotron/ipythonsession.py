# coding: utf-8
import boto3
import sys
import click
session = boto3.Session(profile_name="Liam")
s3 = session.resource("s3")
session.region_name
new_bucket = s3.create_bucket(Bucket='automating-aws-lwr-python')
new_bucket
new_bucket.upload_file("index.html","index.html")
new_bucket.upload_file("webotron/index.html","index.html")
new_bucket.upload_file("webotron/index.html","index.html",ExtraArgs={"ContentType":"text/html"})
import boto3
import sys
import click
session = boto3.Session(profile_name="Liam")

policy = '''{
              "Version":"2012-10-17",
                "Statement":[{
                    "Sid":"PublicReadGetObject",
                    "Effect":"Allow",
                    "Principal": "*",
                    "Action":["s3:GetObject"],
                    "Resource":["arn:aws:s3:::%s/*"]
                    }
                ]
            }''' % new_bucket.name
policy
print(policy)
pol = new_bucket.Policy()
pol
policy = policy.strip()
policy
pol.put(Policy=policy)
ws = new_bucket.Website()
ws.put(WebsiteConfiguration={'ErrorDocument': {
                             'Key': 'error.html' },
                            'IndexDocument': {
                                        'Suffix': 'index.html'})
                                        }

                                        
ws.put(WebsiteConfiguration={'ErrorDocument': {
                             'Key': 'error.html' },
                            'IndexDocument': {
                            'Suffix': 'index.html'}})



url = "https://%s.s3-website.us-east-1.amazonaws.com" % new_bucket.name
