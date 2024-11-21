import pandas as pd
import subprocess
import json
 
# Path to your Excel file
excel_file_path = '/home/abhishek/Downloads/res_tag.xlsx'
 
# Read Excel file
df = pd.read_excel(excel_file_path)
 
# Loop through each row in the DataFrame
for index, row in df.iterrows():
    resource_id = row['ResourceId']
 
    # Prepare new tags
    new_tags = {key: value for key, value in row.items() if key != 'ResourceId'}
 
    # Fetch current tags
    command_fetch = f"az resource show --ids {resource_id} --query tags"
    result = subprocess.run(command_fetch, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Failed to fetch current tags for resource {resource_id}")
        continue
 
    current_tags = json.loads(result.stdout)
 
    # Merge current tags with new tags
    updated_tags = {**current_tags, **new_tags}
 
    # Convert tags to a format suitable for az cli
    tags_cli = ' '.join([f'{key}={value}' for key, value in updated_tags.items()])
 
    # Command to apply merged tags
    command_update = f"az resource tag --ids {resource_id} --tags {tags_cli}"
 
    # Run the command to update tags
    subprocess.run(command_update, shell=True, check=True)
