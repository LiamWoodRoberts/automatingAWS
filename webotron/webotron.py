#!/usr/bin/python

# -*- coding: utf-8 -*-

"""Webotron automates process of deploying static websites to aws
- Configure AWS S3 buckets
    - Create them
    - Set them up
    - Deploy local files to them
- Configure DNS with AWS Route 53
- Configure a Content Delivery Network and SSL with AWS"""

import boto3
import sys
import click

from pathlib import Path
from webotron.bucket import BucketManager

session= None
bucket_manager = None

@click.group()
@click.option('--profile',default=None,help = "Use a given AWS profile.")
def cli(profile):
    '''Webotron deploys websites to AWS'''
    global session,bucket_manager
    session_cfg = {}
    if profile:
        session_cfg["profile_name"] = profile
    session = boto3.Session(**session_cfg)
    bucket_manager = BucketManager(session)
    pass


@cli.command("list-buckets")
def list_buckets():
    '''List all s3 buckets'''
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command("list-bucket-objects")
@click.argument('bucket')
def list_bucket_objects(bucket):
    '''List objects in an s3 bucket'''
    for obj in bucket_manager.all_objects(bucket):
        print(obj)
    pass


@cli.command("setup-bucket")
@click.argument("bucket_name")
def setup_bucket(bucket_name):
    '''Create and configure S3 bucket'''
    s3_bucket = bucket_manager.init_bucket(bucket_name)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3_bucket)

@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket_name')
def sync(pathname, bucket_name):
    "Sync contents of PATHNAME to BUCKET"
    bucket_manager.sync(bucket_name,pathname)
    print(bucket_manager.get_bucket_url(bucket_manager.s3.Bucket(bucket_name)))

if __name__ == "__main__":
    cli()
