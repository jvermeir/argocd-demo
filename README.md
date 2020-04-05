# ArgoCD 101

## Install 

TODO
extra:  kubectl port-forward svc/argocd-server -n argocd 8080:443

## Test 

See https://argoproj.github.io/argo-cd/getting_started/

argocd app create argocd-demo --repo https://github.com/argoproj/argocd-example-apps.git --path guestbook --dest-server https://kubernetes.default.svc --dest-namespace default

kubectl port-forward svc/guestbook-ui 8091:8000