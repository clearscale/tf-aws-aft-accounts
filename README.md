# AFT: Account Definitions

This repository contains the [Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html) account definitions which are deployed via CodePipeline through Control Tower. As described in the [AFT Code Repositories](https://github.com/clearscale/tf-aws-aft?tab=readme-ov-file#aft-code-repositories) section in the main AFT repo, AFT is a [GitOps](https://en.wikipedia.org/wiki/DevOps#:~:text=referenced%20as%20examples.-,GitOps,rolled%20back%20using%20version%2Dcontrolling.) solution and this is one of the five repositories related to deploying and managing accounts in AWS.

## Overview

All accounts created and managed by AFT are located in the [terraform](./terraform/) folder. All terraform files will be sourced from this location. Any account definitions that *will* be needed, but should not be deployed yet go in the [not_used_yet](./not_used_yet/) directory. Additionally, we have made it easy to generate account definitions without the need to know Terraform. In the [scripts](./scripts/) directory, one will find a [accounts.csv](./scripts/accounts.csv) file where all accounts in their required information can be defined in CSV format.

https://docs.aws.amazon.com/controltower/latest/userguide/aft-getting-started.html

## What belongs in here?

AFT Account definitions, described in Terraform code, for AWS accounts that should automatically be deployed and managed by AWS Control Tower.

## What belongs in AFT?

Terraform or scripts that facilitate account-specific definitions or customizations. For instance, when a new account is provisioned through AFT, there might be a requirement to deploy an IAM role to one account immediately upon its creation, whereas the same IAM role may not be necessary for another account. This illustrates the key application for the [AFT Account Customization](https://github.com/clearscale/tf-aws-aft-customization-account) repository.

See also: [What belongs in AFT?](https://github.com/clearscale/tf-aws-aft?tab=readme-ov-file#what-belongs-in-aft) in the main AFT repository.

## What does *not* belong in AFT?

Non-essential or non-foundational resources that are not related to account setup are outside the scope of all AFT repositories. The aim is to maintain the AFT framework with a minimal a footprint.

## Creating new account

To create a new account, create a new `.tf` file with the account name and update the following values

- The value of the terraform module name must be unique per the AWS account request.
  e.g. `module "common-non-prod"`

- The value of module source is the path to the account request Terraform module that AFT provides.

- The value of control_tower_parameters captures the required input to create an AWS Control Tower account. The value includes the following input fields:

  - AccountEmail
  - AccountName
  - ManagedOrganizationalUnit
    - The format for nested OUs should be `dev (ou-ABCD-1234567)`
  - SSOUserEmail
  - SSOUserFirstName
  - SSOUserLastName

- **account_tags** captures user-defined keys and values, which can tag AWS accounts according to business criteria. For more information, see Tagging AWS Organizations resources in the AWS Organizations User Guide.

- The value of **change_management_parameters** captures additional information, such as why an account request was created and who initiated the account request. The value includes the following input fields:

  - change_reason
  - change_requested_by

- **custom_fields** captures additional metadata with keys and values that deploy as SSM parameters in the vended account under `/aft/account-request/custom-fields/`. You can reference this metadata during account customizations to deploy proper controls. For example, an account that's subject to regulatory compliance might deploy additional AWS Config Rules. The metadata that you collect with custom_fields can invoke additional processing during account provisioning and updating. If a custom field is removed from the account request, the custom field is removed from the SSM Parameter Store for the vended account.

- **account_customizations_name** captures the account template folder in the [tf-aws-aft-customizations](https://github.com/clearscale/tf-aws-aft-customization-account) repository.

## Running pipelines via Step Functions

AFT provides an AWS Step Function called `aft-invoke-customizations` in the AFT management account. The purpose of that function is to re-invoke the customization pipeline for AFT-provisioned accounts.

Here is the full event schema (JSON format) you can create to pass input to the `aft-invoke-customizations` AWS Step Function.

```json
{
  "include": [
    {
      "type": "all"
    },
    {
      "type": "ous",
      "target_value": ["ou1", "ou2"]
    },
    {
      "type": "tags",
      "target_value": [{ "key1": "value1" }, { "key2": "value2" }]
    },
    {
      "type": "accounts",
      "target_value": ["acc1_ID", "acc2_ID"]
    }
  ],

  "exclude": [
    {
      "type": "ous",
      "target_value": ["ou1", "ou2"]
    },
    {
      "type": "tags",
      "target_value": [{ "key1": "value1" }, { "key2": "value2" }]
    },
    {
      "type": "accounts",
      "target_value": ["acc1_ID", "acc2_ID"]
    }
  ]
}
```

Below are more specfic examples

All:

```json
{
  "include": [
    {
      "type": "all"
    }
  ]
}
```

Per account

```json
{
  "include": [
    {
      "type": "accounts",
      "target_value": ["12345678912"]
    }
  ]
}
```

Per OU, for **top level OUs, directly under ROOT OU**

```json
{
  "include": [
    {
      "type": "ous",
      "target_value": ["non-prod"]
    }
  ]
}
```

Per OU, for **nested OUs**

```json
{
  "include": [
    {
      "type": "ous",
      "target_value": ["dev (ou-ABCD-1234567)"]
    }
  ]
}
```

Note, you can "mix and match" OU formats

```json
{
  "include": [
    {
      "type": "ous",
      "target_value": ["prod", "stage (ou-XYZ-789010)"]
    }
  ]
}
```

## AFT Code Repositories

1. [Primary AFT Module](https://github.com/clearscale/tf-aws-aft)
2. [Account Definitions](https://github.com/clearscale/tf-aws-aft-accounts)
3. [Account Customizations](https://github.com/clearscale/tf-aws-aft-customization-account)
4. [Global Account Customizations](https://github.com/clearscale/tf-aws-aft-customization-global)
5. [Account Provisioning Customizations](https://github.com/clearscale/tf-aws-aft-customization-account-provisioning)