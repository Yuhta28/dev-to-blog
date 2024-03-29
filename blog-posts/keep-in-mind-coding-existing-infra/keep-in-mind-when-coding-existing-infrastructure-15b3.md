---
title: Keep in mind when coding existing infrastructure
published: true
description:
tags: terraform, aws, devops
---

## Introduction

Many DevOps engineers would like to accomplish our existing cloud infrastructure using code.

However, it is difficult to manage existing infrastructure using code because there are few means and many constraints.

I share this post about getting into the trouble when I challenge the existing AWS infrastructure using code.

## Which infrastructure as code tool

I survey what tools are most suitable for coding our existing AWS infrastructure.

I choose these three as candidates because they have a lot of documentation and articles and a low threshold for learning.

- AWS CloudFormation
- AWS CDK
- Terraform

As a point of selection, I focus on whether or not these three things could be achieved.

- Difficulty in coding existing resources
- Readability of source code
- Scalability for future operations[^1]

[^1]: In the future, I would like build on CI/CD with IaC tool, and it will be automatically deployed and the infrastructure resources will be updated when I `git push` it.

### AWS CloudFormation

https://aws.amazon.com/cloudformation/

CloudFormation is a service that gives developers and businesses an easy way to create a collection of related AWS. Because of AWS service with a long history, there are many cases about IaC. However, when importing existing resources, I give up on coding existing resources because I have to prepare a template file suitable for the resource in advance.

### AWS CDK

https://aws.amazon.com/cdk/

AWS CDK is an open-source software development framework to define your cloud application resources using familiar programming languages.

In Jan 2022, AWS CDK supports below programming languages.

- JavaScript
- TypeScript
- Python
- Java
- C#
- Go (in Developer Preview)

It is very helpful to define the infrastructure resources with my familiar programming languages. But, few people in our team can use programming languages supported by AWS CDK and AWS CDK does not have a function of import existing resources, so that I give up, too.

### Terraform

https://www.terraform.io/

Finally, I decided to manage our infrastructure using code with Terraform.

Although Terraform has a sub-command`import`, the sub-command cannot import multiple resources such as EC2, VPC, and RDS at once, so that it became very hard when the number of target resources was large. So I use `terraformer` to import the existing resources. https://github.com/GoogleCloudPlatform/terraformer

## Point of trouble

However, I still had some problems with the existing resources, so I introduce those parts.

### Version differences between Terraform and terraformer

```bash
$ terraform --version
Terraform v1.1.3
on linux_amd64
$ cat terraform.tfstate | jq -r '. | { terraform_version: .terraform_version }'
{
  "terraform_version": "0.12.31"
}
```

Terraform converts infrastructure resources to IaC based on a file called `.tfstate`, which stores infrastructure resource configuration information. However, the `.tfstate` file generated by terraformer when importing existing resources has an old version of 0.12. If I run command `terraform init` with this file, I will get an error due to version conflicts and will not be able to run Terraform.

```bash
$ terraform init

Initializing the backend...
╷
│ Error: Invalid legacy provider address
│
│ This configuration or its associated state refers to the unqualified provider "aws".
│
│ You must complete the Terraform 0.13 upgrade process before upgrading to later versions.
```

To solve this, I upgrade to version 1 of terraformer's tfstate file to use `tfenv`,Terraform version manage https://github.com/tfutils/tfenv

#### 0.12 -> 0.13

```bash
$ cd #<The directory where the tfstate file exists>
$ tfenv use 0.13.7
$ terraform init
$ terraform plan
$ terraform appy
```

#### 0.13 -> 0.14

```bash
$ tfenv use 0.14.11
$ terraform init
$ terraform plan
$ terraform apply
```

#### 0.14 -> 1.1

```bash
$ tfenv use 1.1.4
$ terraform init
$ terraform plan
$ terraform apply
```

### AWS resources that cannot be imported

The terraformer can import not all AWS resources, and it can import only the resources listed in the below command.

```bash
$ terraformer import aws list
accessanalyzer
acm
alb
api_gateway
appsync
auto_scaling
batch
budgets
cloud9
cloudformation
cloudfront
cloudhsm
cloudtrail
cloudwatch
codebuild
codecommit
codedeploy
codepipeline
cognito
config
customer_gateway
datapipeline
devicefarm
docdb
dynamodb
ebs           #Pay attention to EBS
ec2_instance
ecr
ecrpublic
ecs
efs
eip
eks
elastic_beanstalk
elasticache
elb
emr
eni
es
firehose
glue
iam
igw
iot
kinesis
kms
lambda
logs
media_package
media_store
msk
nacl
nat
opsworks
organization
qldb
rds
resourcegroups
route53
route_table
s3
secretsmanager
securityhub
servicecatalog
ses
sfn
sg
sns
sqs
ssm
subnet
swf
transit_gateway
vpc
vpc_peering
vpn_connection
vpn_gateway
waf
waf_regional
workspaces
xray
```

Although not all AWS resources are supported, all major AWS resources are available, so I thought there would be no problem in this case. However, I could not import EBS even though it was in the list.

```bash
$ terraformer import aws -r ebs
2022/01/16 14:25:57 aws importing default region
2022/01/16 14:25:59 aws importing... ebs
2022/01/16 14:25:59 aws done importing ebs
2022/01/16 14:25:59 Number of resources for service ebs: 0 # no import
2022/01/16 14:25:59 aws Connecting....
2022/01/16 14:25:59 aws save ebs
2022/01/16 14:25:59 aws save tfstate for ebs
```

As a solution, I'm going to manage EBS to code manually `tf` file.

## Conclusion

It turns out that existing resources using code is more difficult than I thought. My goals for this year is our existing resources using code and to spread code-managed infrastructure operations within the our team.

I'll do my best.

## References

https://harness.io/blog/infrastructure-as-code/ https://aws.amazon.com/cloudformation/faqs/ https://www.terraform.io/language/upgrade-guides/1-0

## Original

https://zenn.dev/yuta28/articles/iac-existing-infrastructure
