import boto3
import json
#from boto3_type_annotations.ec2 import Client

#https://docs.amazonaws.cn/en_us/AmazonCloudWatch/latest/events/EventTypes.html#trusted-advisor-event-types

def lambda_handler(event, context):
    print(json.dumps(event))
    check_name = event['detail']['check-name'];
    region = event['detail']["check-item-detail"]["Region"];
    snapshotid = event['detail']["check-item-detail"]["Snapshot ID"];

    #client: Client = boto3.client('ec2',region_name=region)
    client = boto3.client('ec2',region_name=region)
    response = client.modify_snapshot_attribute(
        Attribute='createVolumePermission',
        GroupNames=['all'],
        OperationType='remove',
        SnapshotId=snapshotid,
    )
    print(response)
    return None