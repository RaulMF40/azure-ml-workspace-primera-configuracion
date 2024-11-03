from azure.identity import AzureCliCredential
from azure.ai.ml import MLClient
import os
from dotenv import load_dotenv

load_dotenv()

subscription_id = os.getenv("SUBSCRIPTION_ID")
resource_group = os.getenv("RESOURCE_GROUP")
workspace = os.getenv("WORKSPACE")

# Usar explícitamente AzureCliCredential
credential = AzureCliCredential()
ml_client = MLClient(credential, subscription_id, resource_group, workspace)

print(f"Conectado al workspace: {ml_client.workspace_name}")
print("Conexión exitosa.")
