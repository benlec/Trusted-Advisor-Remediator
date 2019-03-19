import json
import boto3

def getallocidfrompublicip(region,publicip):
    ec2 = boto3.client('ec2', region_name=region)

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_addresses
    response = ec2.describe_addresses(
        Filters=[
            {
                'Name': 'domain',
                'Values':['vpc']
            },
            ],
        PublicIps=[publicip]
        )
    print("result from getallocationidfrompublicip: ",response["Addresses"][0]["AllocationId"])
    
    return response["Addresses"][0]["AllocationId"]

def releaseeip(region, allocationid):
    ec2 = boto3.client('ec2', region_name=region)

    response = ec2.release_address(
        AllocationId=allocationid
        )
    return None


def lambda_handler(event, context):
    print(json.dumps(event))
    check_name = event['detail']['check-name'];
    region = event['detail']["check-item-detail"]["Region"];
    ipaddress = event['detail']["check-item-detail"]["IP Address"];
    ta_success_msg = 'Successfully got details from Trusted Advisor check, %s and executed automated action.' % check_name
    # Retrieve AllocationId from the Event raised by TA
    allocid = getallocidfrompublicip(region, ipaddress)
    print("allocid: ", allocid)
    # Releasing EIP
    releaseeip(region,allocid)
    print (ta_success_msg)
    return None
    