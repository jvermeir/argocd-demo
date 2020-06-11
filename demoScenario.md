# Demo ArgoCD and Kubernetes: ​

## Setup

After install, show argocd namespace

    kubectl get all -n argocd​

To make it accessible in a browser we need a port forwarding rule: ​

    kubectl port-forward svc/argocd-server -n argocd 8080:443 &​

Now open in browser

    https://localhost:8080​

## Get deployments using argocd command line: ​

    argocd app list​

    argocd app create more-helm-stuff \
        --repo https://github.com/jvermeir/argocd-demo.git \
        --path more-helm-stuff \ 
        --dest-server https://kubernetes.default.svc \
        --dest-namespace default ​

    argocd app get more-helm-stuff​

## Test container 

Test container date-time (see `../test-container`)

    docker run -d -p  9123:8000 jvermeir/date-time:1.0.4 123​

    curl localhost:9123​

## Helm chart 

Note Chart.yaml​ defines Helm chart` 
Values.yaml is more or less default, defines some interesting properties like 

    image:
      repository: index.docker.io/jvermeir/date-time
      tag: 1.0.4

`{{ .Values.image.repository }}` and `{{ .Values.image.tag }}` are taken from values.yaml

Services are defined in `templates\the\one` and `templates\the-other`. b****y templating, but this is basically Kubernetes 
where Helm substitutes values from Chart.yaml and values.yaml. Note `templates\_helpers.tpl` defines stuff we can use 
in the template file, like `.Release.Name`.​

Each folder in templates defines both a service and a deployment. The service exposes endpoints implemented by the container in the deployment.

## Deploy 

To force deployment immediately (you can also wait for ArgoCD to pick up the change):

    argocd app sync --prune more-helm-stuff

Add forwarding rules to make the services accessible:

    kubectl port-forward svc/the-one 8092:92 &​
    
    kubectl port-forward svc/the-other 8093:93 &​

Test:

    # this shows: the-one <timestamp> <container short hash> 
    curl localhost:8092​
        
    # this shows: the-other <timestamp> <container short hash> 
    curl localhost:8093​

​The texts `the-one` and `the-other` are defined in the deployment.yaml files for the two services. 

​
