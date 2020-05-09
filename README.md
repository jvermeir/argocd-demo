# ArgoCD 101

## Install 

Do steps 1 and 2 described here:

    See https://argoproj.github.io/argo-cd/getting_started/

To get access to the Argo ui, use port forwarding. run this in a terminal:

    kubectl port-forward svc/argocd-server -n argocd 8080:443 &

login

    # get password
    kubectl get pods -n argocd -l app.kubernetes.io/name=argocd-server -o name | cut -d'/' -f 2

    argocd login localhost:8080
    
Access Argo web ui: open http://localhost:8080 in a private window    
     
## Test 

Create ArgoCD app based on a simple Python http server running in a Docker container. The image is stored on Docker hub.

    argocd app create argocd-demo --repo https://github.com/jvermeir/argocd-demo.git --path date_time --dest-server https://kubernetes.default.svc --dest-namespace default

Port forward so we can access the service

    kubectl port-forward svc/date-time-ui 8081:81
    
Access service:
    
    curl http://localhost:8081/
    
## Build date-time demo service

This ArgoCD project uses a simple http service that returns the current date and time. It is available from Docker hub. 
The Docker container is referenced in `date_time/date-time-ui-deployment.yaml`, change to your own demo if necessary.

```bash
cd date-time
./build.sh <version identifier>
```

where `version identifier` is a random string that identifies this version.

## More experiments

deploy app named `more-helm-stuff` based on a folder of the same name

    argocd app create more-helm-stuff --repo https://github.com/jvermeir/argocd-demo.git --path more-helm-stuff --dest-server https://kubernetes.default.svc --dest-namespace default --upsert

more-helm-stuff has two services, v1 and v2, both based on the date-time test container. The containers can be identified by their return value.
The return value includes a label that is set as an argument to the container in v1-deployment.yaml and v2-deployment.yaml.

delete an app 

    argocd app delete more-helm-stuff
    
update app

    argocd app sync more-helm-stuff
    
        