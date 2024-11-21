# AWS Resource Tagging Script

This script tags AWS resources listed in a CSV file using the `boto3` library. It supports tagging for various AWS services such as EC2, S3, RDS, and more.

## Prerequisites

1. **Python 3.6+**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **AWS CLI**: Install and configure the AWS CLI with your credentials. You can follow the installation guide [here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

3. **AWS IAM Role/Policy**: Ensure you have the necessary permissions to tag resources. The following policy grants the necessary permissions:
    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "resourcegroupstaggingapi:TagResources",
                    "s3:GetBucketLocation",
                    "s3:HeadBucket",
                    "s3:PutBucketTagging"
                ],
                "Resource": "*"
            }
        ]
    }
    ```

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://codebase.aps1aws.lumiq.int/abdul.raheem/CostOps-Templates.git
    cd CostOps-Templates/AWS/Tagging-Resources/
    ```

2. **Create a Virtual Environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the Required Packages**:
    ```bash
    pip install boto3 pandas
    ```

## Usage

1. **Prepare Your CSV File**:
    - Ensure your CSV file (`Sample.csv`) contains the following columns:
        - `Identifier`: The resource identifier (e.g., instance ID, bucket name).
        - `Service`: The AWS service (e.g., EC2, S3).
        - `Type`: The resource type (e.g., Instance, Bucket).
        - `Owner`, `Environment`, `Module`, `Sub-module`, `Project Name`, `Name`: Tags to apply.

2. **Run the Script**:
    - Place your CSV file in the same directory as the script.
    - Run the script:
        ```bash
        python tagging-resources.py
        ```

## Script Explanation

The script performs the following steps:

1. **Load the CSV File**: Reads the CSV file containing the resource details and tags.
    ```python
    csv_file_path = 'Sample.csv'
    df = pd.read_csv(csv_file_path)
    ```

2. **Initialize boto3 Clients**: Initializes `boto3` clients for resource tagging and S3 operations.
    ```python
    tagging_client = boto3.client('resourcegroupstaggingapi', region_name='ap-south-1')
    s3_client = boto3.client('s3', region_name='ap-south-1')
    ```

3. **Helper Functions**:
    - `get_bucket_region(bucket_name)`: Retrieves the region of an S3 bucket.
    - `bucket_exists(bucket_name)`: Checks if an S3 bucket exists in the correct region.
    - `tag_s3_bucket(bucket_name, tags)`: Tags an S3 bucket.
    - `generate_arn(service, resource_id, resource_type)`: Generates ARNs for various AWS resources.
    - `tag_resource(resource_arn, tags)`: Tags a resource using its ARN.

4. **Iterate and Tag Resources**: Iterates over the CSV rows and tags each resource.
    ```python
    for index, row in df.iterrows():
        resource_id = row['Identifier']
        service = row['Service']
        resource_type = row['Type']
        tags = {
            'Owner': row['Owner'],
            'Environment': row['Environment'],
            'Module': row['Module'],
            'Sub-module': row['Sub-module'],
            'Project Name': row['Project Name'],
            'Name': row['Name']
        }
        resource_arn = generate_arn(service, resource_id, resource_type)
        if service == 'S3' and resource_type == 'Bucket':
            tag_s3_bucket(resource_id, tags)
        elif resource_arn:
            tag_resource(resource_arn, tags)
        else:
            print(f"Unsupported resource type for {resource_id}")
    ```

## Conclusion

By following these steps, you can tag AWS resources efficiently using the provided script. Ensure your CSV file is formatted correctly and you have the necessary AWS permissions to perform tagging operations.

