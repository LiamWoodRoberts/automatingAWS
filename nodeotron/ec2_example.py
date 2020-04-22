# coding: utf-8
import boto3
import os
import stat

# Create Session
session = boto3.Session(profile_name="Liam")
ec2 = session.resource('ec2')

# Creating SSH Key
key_name = 'ec2_automation_key'
key_path = key_name + ".pem"
key = ec2.create_key_pair(KeyName=key_name)
with open(key_path,'w') as f:
    f.write(key.key_material)
os.chmod(key_path,stat.S_IRUSR |stat.S_IWUSR)

# Creating EC2 Instance
ec2.images.filter(Owners=['amazon'])
img = ec2.Image("ami-0323c3dd2da7fb37d")
ami_name = 'amzn2-ami-hvm-2.0.20200406.0-x86_64-gp2'
filters = [{"Name":"name","Values":[ami_name]}]
instances = ec2.create_instances(ImageId = img.id,MinCount=1,MaxCount=1,InstanceType='t2.micro',KeyName=key.key_name)
inst = instances[0]
inst.reload()

# Configure SecurityGroup
sg = ec2.SecurityGroup(inst.security_groups[0]["GroupId"])

# ssh for personal IP
sg.authorize_ingress(IpPermissions=[{"FromPort":22,"ToPort":22,"IpProtocol":"TCP","IpRanges":[{"CidrIp":"162.222.59.204/32"}]}])

# HTTP for all
sg.authorize_ingress(IpPermissions=[{"FromPort":80,"ToPort":80,"IpProtocol":"TCP","IpRanges":[{"CidrIp":"0.0.0.0/0"}]}])
