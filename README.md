# Kubernetes Cluster Setup on Azure AKS

## Overview

This repository contains the configuration and setup files for deploying a production-ready Kubernetes cluster on Azure AKS. The cluster is configured with RBAC enabled, two services, and an Ingress controller to manage traffic routing.

## Cluster Details

1. **Cloud Provider**: Azure
2. **Kubernetes Service**: AKS
3. **Cluster Configuration**:
   - **RBAC**: Enabled
   - **Services**:
     - **Service-A**: Retrieves and prints Bitcoin value in dollars every minute. Also prints the average value of the last 10 minutes every 10 minutes.
     - **Service-B**: Prints "Hello Microsoft!" or maintains default behavior.
   - **Ingress Controller**:
     - **Ingress Rules**:
       - `xxx/service-A` -> Service-A
       - `xxx/service-B` -> Service-B
   - **Network Policy**:
     - Service-A cannot communicate with Service-B.

## Repository Structure

- Kubernetes cluster templates for AKS.
- Kubernetes deployment YAML files for services and Ingress controller.
- `service-A/`: Application code and Dockerfile for Service-A.
- `service-B/`: Application code and Dockerfile for Service-B.

## Current Status:

1. **Services**:
 - Both services run ok from the cluster.
 
   ```bash
   kubectl exec -it -n ingress-nginx $(kubectl get pods -n ingress-nginx -o jsonpath='{.items[0].metadata.name}') -- curl http://abservices.westus.cloudapp.azure.com/service-A
   kubectl exec -it -n ingress-nginx $(kubectl get pods -n ingress-nginx -o jsonpath='{.items[0].metadata.name}') -- curl http://abservices.westus.cloudapp.azure.com/service-B

 - Only service-A has an option to run on external-ip (exposed as loadBalancer, no ingress loadBalancer):
   
   ```bash
    http://13.83.6.221:5000

2. **Ingress**:
   - There is a problem I couldnt solve with Ingress external-ip connectivity.
   ```bash
   External-ip : 13.91.107.186
   Host Name : abservices.westus.cloudapp.azure.com
   

## Usefull commands:

1. **Cluster**:
 - check the current context being used by kubectl:
   ```bash
   kubectl config current-context
 - get services:
   ```bash
   kubectl get services -n default
 - describe services:
   ```bash
   kubectl describe service hello-service -n default

 - get Nodes:
   ```bash
   kubectl get nodes 

2. **YAML update**:
 - after updating YAML file - apply:
   ```bash
   kubectl apply -f bitcoin-deployment.yaml
 
 - check deployment status:
   ```bash
   kubectl get deployments

3. **Pods**:
 - get pods name and status:
   ```bash
   kubectl get pods

  - get pods info and details:
    ```bash
    kubectl describe pod <pod-name>

4. **Ingress**:
 - Get external ip of ingress controller:
   ```bash
   kubectl get services --namespace=ingress-nginx



1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
