## Amazon EBS Public Snapshots Security

### Trusted Advisor Check Description
Checks the permission settings for your Amazon Elastic Block Store (Amazon EBS) volume snapshots and alerts you if any snapshots are marked as public. When you make a snapshot public, you give all AWS accounts and users access to all the data on the snapshot. If you want to share a snapshot with particular users or accounts, mark the snapshot as private, and then specify the user or accounts you want to share the snapshot data with. Note: Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear..

### Setup and Usage
You can automatically remove EBS snapshots for volumes that do not have a recent backup as recommended by Trusted Advisor using Amazon Cloudwatch events and AWS Lambda using the following instructions:

1. Create an Amazon IAM role for the Lambda function to use. Make sure this Role has **sufficient execution rights to modify EBS Snapshots**.
Documentation on how to create an IAM policy is available here: http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html
Documentation on how to create an IAM role for Lambda is available here: http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console

2. Create a **Lambda Python** 3.7 function using the [sample](DisableEbsSnapshotPublicAccess.py) provided and choose the IAM role created in step 1. Make sure to set the appropriate tags and region per your requirements in configuration section of the Lambda function. 
More information about Lambda is available here: http://docs.aws.amazon.com/lambda/latest/dg/getting-started.html

3. Create a Cloudwatch event rule to trigger the Lambda function created in step 2 matching the **ERROR status** and the **Amazon EBS Public Snapshot** Trusted Advisor check. An example of this is highlighted in the sample [Cloudwatch Event Pattern](eventsample_ebspublicsnap.json).
Documentation on to create a Trusted Advisor Cloudwatch events rule is available here: http://docs.aws.amazon.com/awssupport/latest/user/cloudwatch-events-ta.html

More information about Trusted Advisor is available here: https://aws.amazon.com/premiumsupport/trustedadvisor/

Please note that this is a just an example of how to setup automation with Trusted Advisor, Cloudwatch and Lambda. We recommend testing it and tailoring to your environment before using in your production envirnment. 

