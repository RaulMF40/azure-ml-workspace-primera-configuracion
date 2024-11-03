#!/bin/bash

# az login
export RESOURCE_GROUP="BootCampDP-100AZURE"
export WORKSPACE_NAME="bootcamp-dp100"

az extension remove -n azure-cli-ml
az extension remove -n ml
az extension add -n ml -y
az group create --name "$RESOURCE_GROUP" --location "eastus"
az ml workspace create --name "$WORKSPACE_NAME" -g "$RESOURCE_GROUP"