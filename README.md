# ArgoCD 101

## Install 

Do steps 1-4 described here:

    See https://argoproj.github.io/argo-cd/getting_started/

To get access to the Argo ui, run this in a terminal:

    kubectl port-forward svc/argocd-server -n argocd 8080:443 &

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
./build.sh
```
    