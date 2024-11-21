import boto3
import datetime

# Define variables
account_id = boto3.client('sts').get_caller_identity().get('Account')
budget_name = "daily-budget-alert"
budget_limit = 150
alert_threshold = 100
email_recipients = ["abdul.raheem@lumiq.ai", "abhishek.sharma1@lumiq.ai"]  # List of email addresses

# Initialize the boto3 client for AWS Budgets
budgets_client = boto3.client('budgets')

# Create a budget
create_budget_response = budgets_client.create_budget(
    AccountId=account_id,
    Budget={
        'BudgetName': budget_name,
        'BudgetLimit': {
            'Amount': str(budget_limit),
            'Unit': 'USD'
        },
        'TimeUnit': 'DAILY',
        'BudgetType': 'COST',
        'TimePeriod': {
            'Start': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            'End': (datetime.datetime.utcnow() + datetime.timedelta(days=365)).strftime('%Y-%m-%dT%H:%M:%SZ')
        },
        'CostTypes': {
            'IncludeTax': False,
            'IncludeSubscription': True,
            'UseBlended': False,
            'IncludeRefund': False,
            'IncludeCredit': False,
            'IncludeUpfront': False,
            'IncludeRecurring': True,
            'IncludeOtherSubscription': True,
            'IncludeSupport': True,
            'IncludeDiscount': True,
            'UseAmortized': False
        }
    },
    NotificationsWithSubscribers=[
        {
            'Notification': {
                'NotificationType': 'ACTUAL',
                'ComparisonOperator': 'GREATER_THAN',
                'Threshold': float(alert_threshold),
                'ThresholdType': 'PERCENTAGE',
            },
            'Subscribers': [
                {
                    'SubscriptionType': 'EMAIL',
                    'Address': email
                } for email in email_recipients
            ]
        }
    ]
)

# Create tags
tags = [
    {
        'Key': 'Name',
        'Value': 'daily-budget-alert'
    },
    {
        'Key': 'Owner',
        'Value': 'Harsh Chaoudhry'
    },
    {
        'Key': 'Project Name',
        'Value': 'Internal'
    }
]

# Tag the budget resource
budgets_client.tag_resource(
    ResourceARN=f"arn:aws:budgets::{account_id}:budget/{budget_name}",
    ResourceTags=tags
)

print("Budget and notification created successfully with tags")