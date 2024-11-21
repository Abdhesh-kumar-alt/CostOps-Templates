from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
import pandas as pd
 
def get_resource_group_from_id(resource_id):
    """Extract the resource group name from the resource ID."""
    return resource_id.split("/")[4]  # The resource group name is the 5th element in the resource ID path
 
try:
    # Initialize the Azure credentials
    credential = DefaultAzureCredential()
 
    # Subscription ID
    subscription_id = 'your-subscription-id'  # Replace with your subscription ID
 
    # Initialize the Resource Management Client
    resource_client = ResourceManagementClient(credential, subscription_id)
 
    # List all resources in the subscription
    resources = resource_client.resources.list()
 
    # Prepare a list to store resource details
    resource_list = []
 
    for resource in resources:
        resource_group = get_resource_group_from_id(resource.id)
        resource_details = {
            'ResourceName': resource.name,
            'ResourceId': resource.id,
            'ResourceType': resource.type,
            'ResourceGroup': resource_group
        }
        resource_list.append(resource_details)
 
    # Convert the list to a DataFrame
    df = pd.DataFrame(resource_list)
 
    # Export the DataFrame to an Excel file
    excel_file_path = '/home/abhishek/Downloads/resources.xlsx'
    df.to_excel(excel_file_path, index=False)
 
    print(f"Resource details have been exported to {excel_file_path}")
 
except Exception as e:
    print(f"An error occurred: {e}")
