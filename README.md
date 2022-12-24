###Docker###

1. Docker build:

docker build . it python-time

2. Docker run

docker run python-time -p 5000:5000

###HELM####

Install Helm:

helm install python-time python-time --namespace <namespace>

Helm Upgrade:

helm upgrade  --version <version> python-time python-time --namespace <namespace>

####Check Kubernetes#### 

kubectl get pods
kubectl get services


####test####

kubectl port-forward <pod id> 5000:5000
curl localhost:5000
