[comment]: # "Auto-generated SOAR connector documentation"
# AWS WAF V2

Publisher: Splunk  
Connector Version: 2\.1\.7  
Product Vendor: AWS  
Product Name: WAF V2  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.10\.0\.40961  

This app integrates with AWS WAF to add and delete IP addresses using API version V2

[comment]: # " File: readme.md"
[comment]: # "  Copyright (c) 2018-2021 Splunk Inc."
[comment]: # ""
[comment]: # "  SPLUNK CONFIDENTIAL - Use or disclosure of this material in whole or in part"
[comment]: # "  without a valid written license from Splunk Inc. is PROHIBITED."
[comment]: # ""
## Asset Configuration

There are two ways to configure an AWS WAF asset. The first is to configure the **access_key** ,
**secret_key** and **region** variables. If it is preferred to use a role and Phantom is running as
an EC2 instance, the **use_role** checkbox can be checked instead. This will allow the role that is
attached to the instance to be used. Please see the [AWS EC2 and IAM
documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)
for more information.

Region parameter provided in the asset configuration parameter and region of the bucket which is
created in AWS console must match, otherwise the user will get an InvalidLocationConstraint error.

For the **Update bucket** action, the
API is unable to validate the KMS key. Hence, it is recommended to provide a
valid KMS key in this action parameter, otherwise it will affect the S3 bucket. For example,
if we update the S3 bucket with an invalid KMS key and run the
'create object' action on the bucket then the action will not work for encryption = NONE.

## Assumed Role Credentials

The optional **credentials** action parameter consists of temporary **assumed role** credentials
that will be used to perform the action instead of those that are configured in the **asset** . The
parameter is not designed to be configured manually, but should instead be used in conjunction with
the Phantom AWS Security Token Service app. The output of the **assume_role** action of the STS app
with data path **assume_role\_\<number>:action_result.data.\*.Credentials** consists of a dictionary
containing the **AccessKeyId** , **SecretAccessKey** , **SessionToken** and **Expiration** key/value
pairs. This dictionary can be passed directly into the credentials parameter in any of the following
actions within a playbook. For more information, please see the [AWS Identity and Access Management
documentation](https://docs.aws.amazon.com/iam/index.html) .


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a WAF V2 asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**access\_key\_id** |  optional  | password | Access Key ID
**access\_key\_secret** |  optional  | password | Access Key Secret
**scope** |  required  | string | Specifies whether this is for an AWS CloudFront distribution or a regional application
**region** |  required  | string | Region
**use\_role** |  optional  | boolean | Use attached role when running Phantom in EC2

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[add ip](#action-add-ip) - Add new IP\(s\) to an existing IP set or a new IP set  
[delete ip](#action-delete-ip) - Remove IP\(s\) from an existing IP set  
[delete ip set](#action-delete-ip-set) - Remove the specified IP Set  
[list acls](#action-list-acls) - List all ACLs  
[list ip sets](#action-list-ip-sets) - List all IP sets  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'add ip'
Add new IP\(s\) to an existing IP set or a new IP set

Type: **contain**  
Read only: **False**

The ip\_set\_id or ip\_set\_name must be given as input for adding an IP to the IP set, ip\_set\_id will be considered if both ip\_set\_id and ip\_set\_name is provided in input\. If the given ip\_set\_name does not exist on the server and the name matches the WAF IP set name criteria, the new IP set with a given input will be created on the server\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip\_set\_id** |  optional  | ID of the IP set | string |  `awswaf ip set id` 
**ip\_set\_name** |  optional  | Name of the IP set | string |  `awswaf ip set name` 
**ip\_address** |  required  | IP Address \(Allows comma\-separated\) | string |  `awswaf ip mask` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.ip\_address | string |  `awswaf ip mask` 
action\_result\.parameter\.ip\_set\_id | string |  `awswaf ip set id` 
action\_result\.parameter\.ip\_set\_name | string |  `awswaf ip set name` 
action\_result\.data\.\*\.Id | string |  `awswaf ip set id` 
action\_result\.data\.\*\.ResponseMetadata\.HTTPHeaders\.content\-length | string | 
action\_result\.data\.\*\.ResponseMetadata\.HTTPHeaders\.content\-type | string | 
action\_result\.data\.\*\.ResponseMetadata\.HTTPHeaders\.date | string | 
action\_result\.data\.\*\.ResponseMetadata\.HTTPHeaders\.x\-amzn\-requestid | string | 
action\_result\.data\.\*\.ResponseMetadata\.HTTPStatusCode | numeric | 
action\_result\.data\.\*\.ResponseMetadata\.RequestId | string | 
action\_result\.data\.\*\.ResponseMetadata\.RetryAttempts | numeric | 
action\_result\.summary\.ip\_status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.NextLockToken | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'delete ip'
Remove IP\(s\) from an existing IP set

Type: **correct**  
Read only: **False**

The ip\_set\_id or ip\_set\_name must be given as input for deleting an IP from the IP set, ip\_set\_id will be considered if both ip\_set\_id and ip\_set\_name is provided in input\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip\_set\_id** |  optional  | IP Set ID | string |  `awswaf ip set id` 
**ip\_set\_name** |  optional  | IP Set Name | string |  `awswaf ip set name` 
**ip\_address** |  required  | IP Address \(Allows comma\-separated\) | string |  `awswaf ip mask` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.ip\_address | string |  `awswaf ip mask` 
action\_result\.parameter\.ip\_set\_id | string |  `awswaf ip set id` 
action\_result\.parameter\.ip\_set\_name | string |  `awswaf ip set name` 
action\_result\.data\.\*\.ResponseMetadata\.HTTPHeaders\.content\-length | string | 
action\_result\.data\.\*\.ResponseMetadata\.HTTPHeaders\.content\-type | string | 
action\_result\.data\.\*\.ResponseMetadata\.HTTPHeaders\.date | string | 
action\_result\.data\.\*\.ResponseMetadata\.HTTPHeaders\.x\-amzn\-requestid | string | 
action\_result\.data\.\*\.ResponseMetadata\.HTTPStatusCode | numeric | 
action\_result\.data\.\*\.ResponseMetadata\.RequestId | string | 
action\_result\.data\.\*\.ResponseMetadata\.RetryAttempts | numeric | 
action\_result\.summary\.ip\_status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.NextLockToken | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'delete ip set'
Remove the specified IP Set

Type: **correct**  
Read only: **False**

The ip\_set\_id or ip\_set\_name must be given as input for deleting an IP set, ip\_set\_id will be used if both ip\_set\_id and ip\_set\_name is provided in input\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip\_set\_id** |  optional  | IP Set ID | string |  `awswaf ip set id` 
**ip\_set\_name** |  optional  | IP Set Name | string |  `awswaf ip set name` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data\.\*\.ResponseMetadata\.RequestId | string | 
action\_result\.data\.\*\.ResponseMetadata\.HTTPHeaders\.date | string | 
action\_result\.data\.\*\.ResponseMetadata\.HTTPHeaders\.content\-type | string | 
action\_result\.data\.\*\.ResponseMetadata\.HTTPHeaders\.content\-length | string | 
action\_result\.data\.\*\.ResponseMetadata\.HTTPHeaders\.x\-amzn\-requestid | string | 
action\_result\.data\.\*\.ResponseMetadata\.RetryAttempts | numeric | 
action\_result\.data\.\*\.ResponseMetadata\.HTTPStatusCode | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.delete\_status | string | 
action\_result\.parameter\.ip\_set\_id | string |  `awswaf ip set id` 
action\_result\.parameter\.ip\_set\_name | string |  `awswaf ip set name` 
action\_result\.parameter\.credentials | string |  `aws credentials` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list acls'
List all ACLs

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**limit** |  optional  | Maximum number of results \(default\: 100\) | numeric | 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.limit | numeric | 
action\_result\.data\.\*\.ARN | string | 
action\_result\.data\.\*\.LockToken | string | 
action\_result\.data\.\*\.Description | string | 
action\_result\.data\.\*\.Name | string | 
action\_result\.data\.\*\.Id | string | 
action\_result\.summary\.number\_of\_acls | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'list ip sets'
List all IP sets

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**limit** |  optional  | Maximum number of results \(default\: 100\) | numeric | 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.limit | numeric | 
action\_result\.data\.\*\.Id | string |  `awswaf ip set id` 
action\_result\.data\.\*\.Name | string |  `awswaf ip set name` 
action\_result\.data\.\*\.ARN | string | 
action\_result\.data\.\*\.LockToken | string | 
action\_result\.data\.\*\.Description | string | 
action\_result\.summary\.number\_of\_ip\_sets | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials` 