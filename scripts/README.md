# Automation Scripts

The following `main.py` script allows you to build terraform files from an account listings in a CSV file.

## Setup

Python 3.x required, with the following libraries
-  os, csv, time, jinja2


## Inputs

The following inputs are required when creating a new AWS account:

- AccountName
- AccountEmail
- ManagedOrganizationalUnit
- SSOUserEmail
- SSOUserFirstName
- SSOUserLastName

NOTE: For Nested OUs, using the following structure

`ManagedOrganizationalUnit = "Sandbox (ou-ab12-abcde123)"`

See more information here:
https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main/sources/aft-customizations-repos/aft-account-request 

## Sample Account structure

Here is a sample AWS Account structure, comprising of 2 OUs, of DEV OU with sandbox and dev account, and PROD

```
── Root
    ├── DEV OU
    │   ├── sandbox
    │   └── dev
    └── PROD OU
        └── Live

```

Here is the above structure in the sample CSV file (shown below with headers)

| AccountName | ManagedOU | AccountEmail             | SSOUserEmail              | SSOUserFirstName | SSOUserLastName |
|-------------|-----------|--------------------------|---------------------------|------------------|-----------------|
| Sandbox     | DEV       | aws-sandbox@customer.com | aws-sandbox1@customer.com | Sandbox          | dev             |
| Dev         | DEV       | aws-dev@customer.com     | aws-dev@customer.com      | Dev              | dev             |
| Live        | PROD      | aws-prod@customer.com    | aws-prod@customer.com     | Live             | prod            |


## Running

To run, simply run the python scripts such as 

`python3 main.py`

The output will be created in a new folder that's timestamped.