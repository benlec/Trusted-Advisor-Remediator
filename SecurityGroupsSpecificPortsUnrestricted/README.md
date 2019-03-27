## Security Groups - Specific Ports Unrestricted

### Trusted Advisor Check Description
Checks security groups for rules that allow unrestricted access (0.0.0.0/0) to specific ports. Unrestricted access increases opportunities for malicious activity (hacking, denial-of-service attacks, loss of data). The ports with highest risk are flagged red, and those with less risk are flagged yellow. Ports flagged green are typically used by applications that require unrestricted access, such as HTTP and SMTP. 
If you have intentionally configured your security groups in this manner, we recommend using additional security measures to secure your infrastructure (such as IP tables). 

### Setup and Usage
One of the possible mitigation for this alert is to perform a cleanup on the unused security groups in your account. You can **automatically "try" to delete the SG mentioned** by Trusted Advisor using Amazon Cloudwatch events and AWS Lambda using the following instructions:

**NB: An error will occur if SG is associated with a ressource so it is safe to try for the deletion. TA checks results will have less false positives after this.**

1. Create an Amazon IAM role for the Lambda function to use. Make sure this Role has **sufficient execution rights to delete SG**.
Documentation on how to create an IAM policy is available here: http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html
Documentation on how to create an IAM role for Lambda is available here: http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console

2. Create a **Lambda Python** 3.7 function using the [sample](SecurityGroupCleanup.py) provided and choose the IAM role created in step 1. Make sure to set the appropriate tags and region per your requirements in configuration section of the Lambda function. 
More information about Lambda is available here: http://docs.aws.amazon.com/lambda/latest/dg/getting-started.html

3. Create a Cloudwatch event rule to trigger the Lambda function created in step 2 matching the **ERROR AND WARN status** and the **Amazon EBS Public Snapshot** Trusted Advisor check. An example of this is highlighted in the sample [Cloudwatch Event Pattern](eventsample_securitygroupspecportunrestr.json).
Documentation on to create a Trusted Advisor Cloudwatch events rule is available here: http://docs.aws.amazon.com/awssupport/latest/user/cloudwatch-events-ta.html

More information about Trusted Advisor is available here: https://aws.amazon.com/premiumsupport/trustedadvisor/

Please note that this is a just an example of how to setup automation with Trusted Advisor, Cloudwatch and Lambda. We recommend testing it and tailoring to your environment before using in your production envirnment. 

