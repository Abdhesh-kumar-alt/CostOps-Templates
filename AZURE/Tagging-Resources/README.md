# Azure Resource Exporter
 
This script exports a list of all Azure resources within a specified subscription to an Excel file. Each resource's name, ID, type, and resource group are included in the output.
 
## Prerequisites
 
1. **Python 3.6 or later**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
 
2. **Azure CLI**: Make sure you have the Azure CLI installed and are logged in. You can download it from [docs.microsoft.com](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
 
3. **Install required Python libraries**: The script requires the `azure-mgmt-resource`, `azure-identity`, `pandas`, and `openpyxl` libraries. You can install them using pip:
 
   ```sh
   pip install azure-mgmt-resource azure-identity pandas openpyxl
   pip install --upgrade pip setuptools
