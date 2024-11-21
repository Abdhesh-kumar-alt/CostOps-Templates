import boto3
import pandas as pd

# Load the updated CSV file
csv_file_path = 'Sample.csv'
df = pd.read_csv(csv_file_path)

# Initialize the boto3 clients with the region ap-south-1
tagging_client = boto3.client('resourcegroupstaggingapi', region_name='ap-south-1')
s3_client = boto3.client('s3', region_name='ap-south-1')

def get_bucket_region(bucket_name):
    """Get the region of an S3 bucket."""
    try:
        response = s3_client.get_bucket_location(Bucket=bucket_name)
        return response['LocationConstraint'] or 'us-east-1'
    except Exception as e:
        print(f"Error getting bucket location for {bucket_name}: {str(e)}")
        return None

def bucket_exists(bucket_name):
    """Check if an S3 bucket exists in the correct region."""
    bucket_region = get_bucket_region(bucket_name)
    if bucket_region != 'ap-south-1':
        print(f"Bucket {bucket_name} is not in the ap-south-1 region.")
        return False
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except s3_client.exceptions.NoSuchBucket:
        return False
    except Exception as e:
        print(f"Error checking existence of bucket {bucket_name}: {str(e)}")
        return False

def tag_s3_bucket(bucket_name, tags):
    if not bucket_exists(bucket_name):
        print(f"Bucket {bucket_name} does not exist or is not in the correct region.")
        return
    try:
        s3_client.put_bucket_tagging(
            Bucket=bucket_name,
            Tagging={'TagSet': [{'Key': k, 'Value': v} for k, v in tags.items()]}
        )
        print(f"Successfully tagged S3 bucket {bucket_name}")
    except Exception as e:
        print(f"Error tagging S3 bucket {bucket_name}: {str(e)}")

def generate_arn(service, resource_id, resource_type):
    """Generate ARNs based on service, resource type, and ID."""
    account_id = '660061364911'  # Replace with your AWS account ID
    region = 'ap-south-1'
    
    if service == 'EC2':
        if resource_type == 'Instance':
            return f'arn:aws:ec2:{region}:{account_id}:instance/{resource_id}'
        elif resource_type == 'Volume':
            return f'arn:aws:ec2:{region}:{account_id}:volume/{resource_id}'
        elif resource_type == 'NetworkInterface':
            return f'arn:aws:ec2:{region}:{account_id}:network-interface/{resource_id}'
        elif resource_type == 'SecurityGroup':
            return f'arn:aws:ec2:{region}:{account_id}:security-group/{resource_id}'
        elif resource_type == 'Snapshot':
            return f'arn:aws:ec2:{region}:{account_id}:snapshot/{resource_id}'
    elif service == 'S3' and resource_type == 'Bucket':
        return f'arn:aws:s3:::{resource_id}'
    elif service == 'RDS' and resource_type == 'DBInstance':
        return f'arn:aws:rds:{region}:{account_id}:db:{resource_id}'
    elif service == 'SecretsManager' and resource_type == 'Secret':
        return f'arn:aws:secretsmanager:{region}:{account_id}:secret:{resource_id}'
    elif service == 'Glue' and resource_type == 'Job':
        return f'arn:aws:glue:{region}:{account_id}:job/{resource_id}'
    elif service == 'CertificateManager' and resource_type == 'Certificate':
        return f'arn:aws:acm:{region}:{account_id}:certificate/{resource_id}'
    elif service == 'CloudFormation' and resource_type == 'Stack':
        return f'arn:aws:cloudformation:{region}:{account_id}:stack/{resource_id}'
    elif service == 'CloudTrail' and resource_type == 'Trail':
        return f'arn:aws:cloudtrail:{region}:{account_id}:trail/{resource_id}'
    elif service == 'CloudWatch' and resource_type == 'Alarm':
        return f'arn:aws:cloudwatch:{region}:{account_id}:alarm/{resource_id}'
    elif service == 'CodeBuild' and resource_type == 'Project':
        return f'arn:aws:codebuild:{region}:{account_id}:project/{resource_id}'
    elif service == 'CodeCommit' and resource_type == 'Repository':
        return f'arn:aws:codecommit:{region}:{account_id}:{resource_id}'
    elif service == 'CodePipeline' and resource_type == 'Pipeline':
        return f'arn:aws:codepipeline:{region}:{account_id}:{resource_id}'
    elif service == 'Cognito' and resource_type == 'UserPool':
        return f'arn:aws:cognito-idp:{region}:{account_id}:userpool/{resource_id}'
    elif service == 'DynamoDB' and resource_type == 'Table':
        return f'arn:aws:dynamodb:{region}:{account_id}:table/{resource_id}'
    elif service == 'ECS' and resource_type == 'Cluster':
        return f'arn:aws:ecs:{region}:{account_id}:cluster/{resource_id}'
    elif service == 'EFS' and resource_type == 'FileSystem':
        return f'arn:aws:elasticfilesystem:{region}:{account_id}:file-system/{resource_id}'
    elif service == 'EKS' and resource_type == 'Cluster':
        return f'arn:aws:eks:{region}:{account_id}:cluster/{resource_id}'
    elif service == 'EMR' and resource_type == 'Cluster':
        return f'arn:aws:elasticmapreduce:{region}:{account_id}:cluster/{resource_id}'
    elif service == 'ElasticBeanstalk' and resource_type == 'Application':
        return f'arn:aws:elasticbeanstalk:{region}:{account_id}:application/{resource_id}'
    elif service == 'ElasticLoadBalancing' and resource_type == 'LoadBalancer':
        return f'arn:aws:elasticloadbalancing:{region}:{account_id}:loadbalancer/{resource_id}'
    elif service == 'ElasticLoadBalancingV2' and resource_type == 'LoadBalancer':
        return f'arn:aws:elasticloadbalancing:{region}:{account_id}:loadbalancer/{resource_id}'
    elif service == 'Events' and resource_type == 'Rule':
        return f'arn:aws:events:{region}:{account_id}:rule/{resource_id}'
    elif service == 'Greengrass' and resource_type == 'Group':
        return f'arn:aws:greengrass:{region}:{account_id}:group/{resource_id}'
    elif service == 'KMS' and resource_type == 'Key':
        return f'arn:aws:kms:{region}:{account_id}:key/{resource_id}'
    elif service == 'Lambda' and resource_type == 'Function':
        return f'arn:aws:lambda:{region}:{account_id}:function:{resource_id}'
    elif service == 'APIGateway' and resource_type == 'RestApi':
        return f'arn:aws:apigateway:{region}::/restapis/{resource_id}'
    elif service == 'Redshift' and resource_type == 'Cluster':
        return f'arn:aws:redshift:{region}:{account_id}:cluster/{resource_id}'
    elif service == 'ResourceGroups' and resource_type == 'Group':
        return f'arn:aws:resource-groups:{region}:{account_id}:group/{resource_id}'
    elif service == 'SageMaker' and resource_type == 'Endpoint':
        return f'arn:aws:sagemaker:{region}:{account_id}:endpoint/{resource_id}'
    elif service == 'SES' and resource_type == 'Identity':
        return f'arn:aws:ses:{region}:{account_id}:identity/{resource_id}'
    elif service == 'SNS' and resource_type == 'Topic':
        return f'arn:aws:sns:{region}:{account_id}:{resource_id}'
    elif service == 'SQS' and resource_type == 'Queue':
        return f'arn:aws:sqs:{region}:{account_id}:{resource_id}'
    elif service == 'SSM' and resource_type == 'ManagedInstance':
        return f'arn:aws:ssm:{region}:{account_id}:managed-instance/{resource_id}'
    elif service == 'StepFunctions' and resource_type == 'StateMachine':
        return f'arn:aws:states:{region}:{account_id}:stateMachine:{resource_id}'
    elif service == 'DMS' and resource_type == 'ReplicationInstance':
        return f'arn:aws:dms:{region}:{account_id}:rep:{resource_id}'
    elif service == 'DataBrew' and resource_type == 'Project':
        return f'arn:aws:databrew:{region}:{account_id}:project/{resource_id}'
    else:
        return None

def tag_resource(resource_arn, tags):
    try:
        tagging_client.tag_resources(
            ResourceARNList=[resource_arn],
            Tags=tags
        )
        print(f"Successfully tagged resource {resource_arn}")
    except Exception as e:
        print(f"Error tagging resource {resource_arn}: {str(e)}")

# Iterate over the rows in the DataFrame
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
    
    # Generate the ARN based on service and type
    resource_arn = generate_arn(service, resource_id, resource_type)
    
    # Tag the resource
    if service == 'S3' and resource_type == 'Bucket':
        tag_s3_bucket(resource_id, tags)
    elif resource_arn:
        tag_resource(resource_arn, tags)
    else:
        print(f"Unsupported resource type for {resource_id}")

