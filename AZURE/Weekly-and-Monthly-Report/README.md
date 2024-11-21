# Cost Report CSV Template Guide

This guide provides the format for the CSV file that should be used to report the monthly and weekly costs for each project. The CSV file should be structured with specific columns to ensure consistency and accuracy in the billing details.

## CSV Template Format

The CSV file should include the following columns for the cost report:

### Basic Template

| CustomerName | ProjectName | CloudProvider | StartDate | EndDate | ServiceName | CostUSD | Environment |
|--------------|-------------|---------------|-----------|---------|-------------|---------|-------------|
|              |             |               |           |         |             |         |             |
|              |             |               |           |         |             |         |             |
|              |             |               |           |         |             |         |             |

### Module Level Template

| CustomerName | ProjectName | CloudProvider | StartDate | EndDate | Module | CostUSD | Environment |
|--------------|-------------|---------------|-----------|---------|--------|---------|-------------|
|              |             |               |           |         |        |         |             |
|              |             |               |           |         |        |         |             |
|              |             |               |           |         |        |         |             |

### SubModule Level Template

| CustomerName | ProjectName | CloudProvider | StartDate | EndDate | Module | SubModule | CostUSD | Environment |
|--------------|-------------|---------------|-----------|---------|--------|-----------|---------|-------------|
|              |             |               |           |         |        |           |         |             |
|              |             |               |           |         |        |           |         |             |
|              |             |               |           |         |        |           |         |             |

## Column Descriptions

- **CustomerName**: The name of the customer for whom the cost report is being generated.
- **ProjectName**: The name of the project associated with the cost.
- **CloudProvider**: The cloud provider (e.g., AWS, Azure, GCP) where the services are hosted.
- **StartDate**: The start date of the billing period in `YYYY-MM-DD` format.
- **EndDate**: The end date of the billing period in `YYYY-MM-DD` format.
- **ServiceName**: The name of the service being billed (only in the Basic Template).
- **Module**: The module associated with the cost (used in the Module Level and SubModule Level Templates).
- **SubModule**: The submodule associated with the cost (only in the SubModule Level Template).
- **CostUSD**: The cost in USD for the specified service/module/submodule.
- **Environment**: The environment (e.g., Development, Staging, Production) where the service/module/submodule is deployed.

## Instructions

1. **Choose the Appropriate Template**: Based on the level of detail required (basic, module, or submodule), select the appropriate template format from above.
2. **Fill in the Details**: Populate the columns with the relevant data for each project and billing period.
3. **Save the File**: Save the completed CSV file with an appropriate name that includes the billing period (e.g., `CostReport_May2024.csv`).
4. **Submit the Report**: Share the completed CSV file with the team lead or designated recipient for review.

## Example

Here is an example of a filled CSV file using the Basic Template:

```csv
CustomerName,ProjectName,CloudProvider,StartDate,EndDate,ServiceName,CostUSD,Environment
AcmeCorp,ProjectA,AWS,2024-05-01,2024-05-31,EC2,100.00,Production
AcmeCorp,ProjectA,AWS,2024-05-01,2024-05-31,S3,50.00,Production
BetaInc,ProjectB,GCP,2024-05-01,2024-05-31,ComputeEngine,200.00,Development

