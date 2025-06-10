# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "975c3a1d-0018-4a7b-9955-97e2d66f5be3",
# META       "default_lakehouse_name": "BPADatalakehouse",
# META       "default_lakehouse_workspace_id": "0a391d74-55ad-41a9-a8bd-51c82c283ec2",
# META       "known_lakehouses": [
# META         {
# META           "id": "975c3a1d-0018-4a7b-9955-97e2d66f5be3"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

%pip install semantic-link-labs

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import sempy_labs as labs

dataset = 'bb236340-ca61-4a51-ae1d-575e16ee1d8c' # Enter the name or ID of your semantic model
workspace = '0a391d74-55ad-41a9-a8bd-51c82c283ec2' # Enter the name or ID of the workspace in which the semantic model resides

#labs.run_model_bpa(dataset=dataset, workspace=workspace)
#labs.run_model_bpa(dataset=dataset, workspace=workspace, extended=True) # Setting extended=True will fetch Vertipaq Analyzer statistics and use them to run advanced BPA rules against your model
#labs.run_model_bpa(dataset=dataset, workspace=workspace, export=True) # Setting export=True will export the results to a delta table in the lakehouse attached to the notebook
labs.run_model_bpa(dataset=dataset, workspace=workspace, language="it-IT") # Setting the 'language' parameter will dynamically translate the rules, categories and descriptions to the specified language.

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
