import boto3
import json
#from boto3_type_annotations.rds import Client
from botocore.exceptions import ClientError

#
# Useful documentation link
# https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html
#

def lambda_handler(event, context):
    print(json.dumps(event))
    check_name = event['detail']['check-name'];
    region = event['detail']["check-item-detail"]["Region"];
    dbinstancename = event['detail']["check-item-detail"]["DB Instance Name"];
    estimatedsavings = event['detail']["check-item-detail"]["Estimated Monthly Savings (On Demand)"];
    
    try:
        #client: Client = boto3.client("rds",region_name=region)
        client = boto3.client("rds",region_name=region)
        response = client.stop_db_instance(
            DBInstanceIdentifier=dbinstancename
        )
        print("Successfully stopped '{}' RDS Instance in region '{}'. Saving you around {} monthly (onDemand Price)".format(dbinstancename,region,estimatedsavings))
    except ClientError as e:
        # We cannot stop AuroraDB because they are clusters. We cannot use stop_cluster as we don't have the cluster ID in event.
        if e.response['Error']['Code'] == 'InvalidParameterCombination': 
            print("Unable to stop database '{}' in region '{}': {}".format(dbinstancename,region,e.response['Error']['Message']))
        else:
            error2raise = "An unexpected errror occured while trying to stop DBInstance: {}".format(e.response)
            raise error2raise
    return None