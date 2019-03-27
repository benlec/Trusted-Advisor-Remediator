import boto3
import json
from botocore.exceptions import ClientError
#from boto3_type_annotations.ec2 import Client

def lambda_handler(event, context):
    print(json.dumps(event))
    check_name = event['detail']['check-name'];
    region = event['detail']["check-item-detail"]["Region"];
    securitygroupname = event['detail']["check-item-detail"]["Security Group Name"];
    securitygroupid = event['detail']["check-item-detail"]["Security Group ID"];
    
    #client: Client = boto3.client("ec2",region_name=region)
    client = boto3.client("ec2",region_name=region)
    try:
        response = client.delete_security_group(
        GroupId=securitygroupid.split(' ')[0],
        GroupName=securitygroupname
        )
        #print(response)
        print("successfully deleted [Name: {}, ID: {}] security group".format(securitygroupname, securitygroupid))
    except ClientError as e:
        if e.response['Error']['Code'] == 'DependencyViolation':
            print("Unable to cleanup security group [Name: {}, ID: {}] because it's currently in use".format(securitygroupname, securitygroupid))
        else:
            error2raise = "An unexpected errror occured while trying to perform cleanup: {}".format(e)
            raise error2raise
    return None