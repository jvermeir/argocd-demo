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

    argocd app create argocd-demo 
        --repo https://github.com/jvermeir/argocd-demo.git \
        --path date_time \
        --dest-server https://kubernetes.default.svc 
        --dest-namespace default

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

## Create chart named `more-helm-stuff` and two services

### step 1, empty app

see https://github.com/jvermeir/argocd-demo.git, checkout tag `basic-app`

Deploy Argo app named `more-helm-stuff` based on a folder of the same name

    argocd app create more-helm-stuff --repo https://github.com/jvermeir/argocd-demo.git --path more-helm-stuff --dest-server https://kubernetes.default.svc --dest-namespace default --upsert

### step 2, add a service named `the-one`

see https://github.com/jvermeir/argocd-demo.git, checkout tag `the-one-service`

Deploy, make sure older versions are removed

    argocd app sync --prune more-helm-stuff

set up a port forward rule so we can access the service

    kubectl port-forward svc/the-one 8092:92 &

See if it works

    curl localhost:8092
    # returns the-one - 2020-05-10 10:34:36.402516 - fe48daf

### step 3, add a service named `the-other`

see https://github.com/jvermeir/argocd-demo.git, checkout tag `the-other-service`

Deploy, make sure older versions are removed

    argocd app sync --prune more-helm-stuff

set up a port forward rule so we can access the service

    kubectl port-forward svc/the-one 8093:93 &

See if it works

    curl localhost:8093
    # returns the-other - 2020-05-10 11:33:42.025367 - fe48daf

## More useful argocd commands

delete
    
    argocd app delete more-helm-stuff
    
get details

    > argocd app list
    
    NAME             CLUSTER                         NAMESPACE  PROJECT  STATUS  HEALTH   SYNCPOLICY  CONDITIONS  REPO                                         PATH             TARGET
    more-helm-stuff  https://kubernetes.default.svc  default    default  Synced  Healthy  Auto        <none>      https://github.com/jvermeir/argocd-demo.git  more-helm-stuff    

more details

    > argocd app get more-helm-stuff
    
    Name:               more-helm-stuff
    Project:            default
    Server:             https://kubernetes.default.svc
    Namespace:          default
    URL:                https://localhost:8080/applications/more-helm-stuff
    Repo:               https://github.com/jvermeir/argocd-demo.git
    Target:
    Path:               more-helm-stuff
    SyncWindow:         Sync Allowed
    Sync Policy:        Automated
    Sync Status:        Synced to  (8373798)
    Health Status:      Healthy
    
    GROUP  KIND        NAMESPACE  NAME       STATUS  HEALTH   HOOK  MESSAGE
           Service     default    the-one    Synced  Healthy        service/the-one unchanged
           Service     default    the-other  Synced  Healthy        service/the-other created
    apps   Deployment  default    the-one    Synced  Healthy        deployment.apps/the-one unchanged
    apps   Deployment  default    the-other  Synced  Healthy        deployment.apps/the-other created        
    
## Argocd in Kubernetes

Deployed in a separate namespace, if you follow the install manual (see above) the namespace is `argocd`.

    > kubectl get pods -n argocd

    NAME                                             READY   STATUS    RESTARTS   AGE
    argocd-application-controller-7c77748d75-r57zm   1/1     Running   64         7d16h
    argocd-dex-server-5666668895-xc8vl               1/1     Running   2          7d16h
    argocd-redis-6d7f9df848-jc7hn                    1/1     Running   2          7d16h
    argocd-repo-server-dfb5c86ff-p4kh5               1/1     Running   3          7d16h
    argocd-server-878dc8cd7-m6hlb                    1/1     Running   49         7d16h