## Amazon RDS Idle DB Instances

### Trusted Advisor Check Description
Checks the configuration of your Amazon Relational Database Service (Amazon RDS) for any DB instances that appear to be idle. If a DB instance has not had a connection for a prolonged period of time, you can delete the instance to reduce costs. If persistent storage is needed for data on the instance, you can use lower-cost options such as taking and retaining a DB snapshot. Manually created DB snapshots are retained until you delete them. Data for Amazon RDS instances created in the Asia Pacific (Seoul) region (sa-east-1) is not available. We are working to fix this issue as soon as possible.

### Setup and Usage
To save cost, one of the solution here is to **STOP the Database detected as Idle**. So this Lambda here will simply stop the RDS Instances mentionned in the TA Event.

**NB: This will not work for Aurora as the TA Event do not provide Aurora Cluster ID**

1. Create an Amazon IAM role for the Lambda function to use. Make sure this Role has **sufficient execution rights to stop RDS instances**.
Documentation on how to create an IAM policy is available here: http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html
Documentation on how to create an IAM role for Lambda is available here: http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console

2. Create a **Lambda Python** 3.7 function using the [sample](Amazon_RDS_Idle_DB_Instances.py) provided and choose the IAM role created in step 1. Make sure to set the appropriate tags and region per your requirements in configuration section of the Lambda function. 
More information about Lambda is available here: http://docs.aws.amazon.com/lambda/latest/dg/getting-started.html

3. Create a Cloudwatch event rule to trigger the Lambda function created in step 2 matching the **WARN status** and the **Amazon RDS Idle DB Instances** Trusted Advisor check. An example of this is highlighted in the sample [Cloudwatch Event Pattern](eventsample_AmazonRDSIdleDBInstances.json).
Documentation on to create a Trusted Advisor Cloudwatch events rule is available here: http://docs.aws.amazon.com/awssupport/latest/user/cloudwatch-events-ta.html

More information about Trusted Advisor is available here: https://aws.amazon.com/premiumsupport/trustedadvisor/

Please note that this is a just an example of how to setup automation with Trusted Advisor, Cloudwatch and Lambda. We recommend testing it and tailoring to your environment before using in your production envirnment. 

