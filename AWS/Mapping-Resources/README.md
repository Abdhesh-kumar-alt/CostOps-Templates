# AWS Resource Mapping Guide

This guide provides the instructions and template for mapping all AWS resources into a CSV file. Follow the steps below to ensure all resources are correctly documented.

## Prerequisites

1. **AWS Management Console Access**: Ensure you have access to the AWS Management Console.
2. **AWS CLI**: Install and configure the AWS CLI with your credentials. You can follow the installation guide [here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
3. **Permissions**: Ensure you have the necessary permissions to list and describe resources in your AWS account.

## CSV Template Format

The CSV file should include the following columns:

| Module                 | Sub-module | Resource Type | Resource Sub-Type | Resource Identifier | Resource Name | Tags | Owner | Environment | Module                 | Sub-module | Project     | Resource Full Name                      |
|------------------------|------------|---------------|-------------------|---------------------|---------------|------|-------|-------------|------------------------|------------|-------------|-----------------------------------------|
| Platform Common Modules| Test       | EC2           | TargetGroup       |                     | policy        |      | Lumiq | UAT         | Platform Common Modules| Test       | Dataverse   | empower-hdfcamc-uat-policy             |
|                        |            |               |                   |                     |               |      |       |             |                        |            |             |                                         |
| Platform Common Modules|            |               |                   |                     |               |      |       |             | Platform Common Modules| 0          | Dataverse   |                                         |
|                        |            |               |                   |                     |               |      |       |             |                        | 0          | Dataverse   |                                         |
|                        |            |               |                   |                     |               |      |       |             |                        | 0          | Dataverse   |                                         |

## Column Descriptions

- **Module**: The main module category (e.g., Platform Common Modules, Ingestion, Processing, Dataxchange, Development).
- **Sub-module**: The sub-module category within the main module.
- **Resource Type**: The type of AWS resource (e.g., EC2, S3, Glue).
- **Resource Sub-Type**: The sub-type of the resource if applicable (e.g., Instance, Bucket, Job).
- **Resource Identifier**: The unique identifier for the resource (e.g., instance ID, ARN).
- **Resource Name**: The name of the resource.
- **Tags**: Any tags associated with the resource.
- **Owner**: The owner of the resource.
- **Environment**: The environment where the resource is deployed (e.g., UAT, Production).
- **Project**: The project associated with the resource.
- **Resource Full Name**: A descriptive name for the resource combining relevant details.

## Instructions

1. **Review the Provided Template**: Familiarize yourself with the template structure and column descriptions provided above.
2. **Identify Resources**: Use the AWS Management Console or AWS CLI to list and describe resources in your account.
3. **Map Resources**: Fill in the CSV file using the template format, ensuring all resources are mapped correctly.
    - Use the **Module** and **Sub-module** values to categorize resources.
    - Provide accurate values for **Resource Type**, **Resource Sub-Type**, and **Resource Identifier**.
    - Include the **Resource Name**, **Tags**, **Owner**, **Environment**, **Project**, and **Resource Full Name** for each resource.

### Example

Here is an example of how to fill in the CSV file:

```csv
Module,Sub-module,Resource Type,Resource Sub-Type,Resource Identifier,Resource Name,Tags,Owner,Environment,Module,Sub-module,Project,Resource Full Name
Platform Common Modules,Test,EC2,TargetGroup,,policy,,Lumiq,UAT,Platform Common Modules,Test,Dataverse,empower-hdfcamc-uat-policy

