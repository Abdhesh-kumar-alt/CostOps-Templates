# Cost Report CSV Template Guide

This guide provides the format for the CSV file that should be used to report the monthly and weekly costs for each project. The CSV file should be structured with specific columns to ensure consistency and accuracy in the billing details.

## CSV Template Format

The CSV file should include the following columns for the cost report:

### Service level Template

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

# AWS Cost by Service Report

This Python script generates a report of AWS costs by service for a specified time period and saves the results to a CSV file.

## Prerequisites

- Python 3.8 or higher
- boto3 library
- pandas library
- AWS credentials configured

## Installation

1. Install the required Python libraries using pip:
    ```sh
    pip install boto3 pandas
    ```

2. Ensure your AWS credentials are configured. You can configure them using the AWS CLI or by setting environment variables.

## Script Details

The script performs the following steps:

1. Configures the AWS Cost Explorer client.
2. Defines the time period and granularity for the cost report.
3. Retrieves cost and usage data from AWS Cost Explorer.
4. Converts the response to a Pandas DataFrame.
5. Saves the DataFrame to a CSV file.

## Usage

1. **Modify the Time Period**: Change the `Start` and `End` dates in the `time_period` dictionary to your desired time range.
    ```python
    time_period = {
        'Start': '2024-05-16',  # Replace with your start date
        'End': '2024-05-31'     # Replace with your end date
    }
    ```

2. **Customize Customer and Project Details**: Replace the `CustomerName`, `ProjectName`, and `Environment` values with actual values relevant to your project.
    ```python
    aws_data.append({
        'CustomerName': 'Lumiq',  # Replace with actual customer name
        'ProjectName': 'LumiqInternal',  # Replace with actual project name
        'CloudProvider': 'AWS',
        'StartDate': result['TimePeriod']['Start'],
        'EndDate': result['TimePeriod']['End'],
        'ServiceName': group['Keys'][0],
        'CostUSD': round(float(group['Metrics']['UnblendedCost']['Amount']), 2),
        'Environment': 'DEV'  # Replace with actual environment
    })
    ```

3. **Specify the Output Filename**: Change the `aws_csv_file` variable to the desired output CSV filename.
    ```python
    aws_csv_file = 'aws_internal_cost_report2.csv'  # Replace with your desired filename
    ```

4. **Run the Script**: Execute the script to generate the cost report.
    ```sh
    python cost_by_service.py
    ```

## Script

```python
import boto3
import pandas as pd

# Configure AWS client
client = boto3.client('ce', region_name='ap-south-1')

# Define the time period and granularity
time_period = {
    'Start': '2024-05-16',
    'End': '2024-05-31'
}

response = client.get_cost_and_usage(
    TimePeriod=time_period,
    Granularity='MONTHLY',
    Metrics=['UNBLENDED_COST'],
    GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
)

# Convert the response to a DataFrame
aws_data = []
for result in response['ResultsByTime']:
    for group in result['Groups']:
        aws_data.append({
            'CustomerName': 'Lumiq',  # Replace with actual customer name
            'ProjectName': 'LumiqInternal',  # Replace with actual project name
            'CloudProvider': 'AWS',
            'StartDate': result['TimePeriod']['Start'],
            'EndDate': result['TimePeriod']['End'],
            'ServiceName': group['Keys'][0],
            'CostUSD': round(float(group['Metrics']['UnblendedCost']['Amount']), 2),
            'Environment': 'DEV'  # Replace with actual environment
        })

aws_df = pd.DataFrame(aws_data)

# Save the AWS data to a CSV file
aws_csv_file = 'aws_internal_cost_report2.csv'
aws_df.to_csv(aws_csv_file, index=False)
print(f"AWS cost report saved to {aws_csv_file}")
```

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

