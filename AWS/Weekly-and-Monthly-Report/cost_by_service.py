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