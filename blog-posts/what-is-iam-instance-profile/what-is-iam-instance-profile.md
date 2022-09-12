---
title: What is IAM Instance Profile?
published: false
description:
tags: AWS, IAM
---

## Introduction

You attach IAM role with IAM policy to AWS resources which granted to operate the other AWS Resources.

![image1](./assets/image3.png)

However, EC2 is not attached to IAM Role, but is attached to IAM Instance Profile.

![image2](./assets/image1.png)

![image3](./assets/image2.png)

In AWS CLI, There is the parameter about `IamInstanceProfile`, too.

```console
 aws ec2 describe-instances --query "Reservations[].Instances[].IamInstanceProfile.Arn"
[
    "arn:aws:iam::XXXXXXXXXXXX:instance-profile/Yuta20210911"
]
```

So, what is the IAM Instance Profile?

## About IAM Insntacen Profile

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html
