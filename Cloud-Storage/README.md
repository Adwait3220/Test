his template creates an instance template, instance-group and required dependencies to create load balancer using deployment manager.

## Prerequisites
- Install gcloud
- Create a GCP project, setup billing, enable requisite APIs
- Grant the compute.admin IAM role to the Deployment Manager service account in case you are using custom service account.

## Deployment
## Resources
- storage-v1.buckets

## Usage
Clone the Deployment Manager samples repository
```shell
    git clone https://github.com/Adwait3220/Test/new/main/Cloud-Storage
```
- Open GCP CLI or Cloudshell and set the project if not selected
- Create your deployment as described below, replacing <YOUR_DEPLOYMENT_NAME> with your with your own deployment name

```shell
    gcloud deployment-manager deployments create <YOUR_DEPLOYMENT_NAME> --config bucket-config.yaml
```

**note: In case you have created the deployment with the same name kindly delete the older one along with resources to avoid conflict.**
        
        
In case you need to delete your deployment use below command:

```shell
    gcloud deployment-manager deployments delete <YOUR_DEPLOYMENT_NAME>
```
