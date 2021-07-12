# devnet-k8s
k8s manifest files to help in prep for decor and DevOps exams

## Docker Images
The docker image referenced in the manifest files is a simple flask app build on python-slim, stored in a private dockerhub repository.
the multi-container-pod.yml manifest file also includes a second flask app container, listening on port 5001

Dockerfiles are included in the docker folder

## Manifest Files

### simple_pod.yml

creates a pod with a single container running a flash app on port 5000 
/index returns "Hello from Kubernetes POD pod-name"

### multi_container_pod.yml

Demonstrates a Pod running 2 containers
  
### pod_service_clstrIP.yml
  Adds a service to the simple pod using the default ClusterIP service type
  
### pod_service_nodePort.yml
  Demonstrates a service using the NodePort type, showing the app is reachable via a node IP:Port combination
  
### pod_service_configmap.yml
  Demonstrates how to pass environment variables to a Pod using configMaps
  
### deployment.yml
Demonstrates kubernetes deployments to deploy multiple replicas of the pod
  
### deployment_volumes.yml
  Demonstrates volumes using HostPath. A deployment is used to deploy the volume with each pod replica
  
### deployment_vol_configMap.yml
  Extends the volumes example to show how you can use configMaps to add files to the container
  
### deployment_recreate.yml
  Demonstrates Kubernetes ReCreate deployment strategy, i.e. Big Bang
  
### deployment_RollingUpdate.yml
  Demonstrates Kubernetes RollingUpdate deployment strategy
