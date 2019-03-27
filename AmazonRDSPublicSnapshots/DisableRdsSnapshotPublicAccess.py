import boto3
import json
#from boto3_type_annotations.rds import Client

#https://docs.amazonaws.cn/en_us/AmazonCloudWatch/latest/events/EventTypes.html#trusted-advisor-event-types

def lambda_handler(event, context):
    print(json.dumps(event))
    check_name = event['detail']['check-name'];
    region = event['detail']["check-item-detail"]["Region"];
    dbinstanceid = event['detail']["check-item-detail"]["DB Instance or Cluster ID"];
    snapshotarn = event['detail']["check-item-detail"]["Snapshot ID"];

    #client: Client = boto3.client("rds",region_name=region)
    client = boto3.client("rds",region_name=region)
    response = client.modify_db_snapshot_attribute(
        AttributeName='restore',
        DBSnapshotIdentifier=snapshotarn.split(':')[6],
        ValuesToRemove=['all'],
    )
    print(response)
    return None