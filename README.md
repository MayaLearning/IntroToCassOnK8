# TITLE HERE

##  DISCRIPTION HERE
This is a discription of the cool stuff we are going to do in the session today

Banner
<img src="https://user-images.githubusercontent.com/blah/blahblah.png" width=“700” />

## Before starting
Workshop attendees will receave an email with the instance info prior to the workshop.

Notice that training cloud instances will be available only during the workshop and will be terminated **24 hours later**. If you are in our workshop we recommend using the provided cloud instance, you can relax as we have you covered: prerequisites are installed already.

**⚡ IMPORTANT NOTE:**
Everywhere in this repo you see `<YOURADDRESS>` replace with the URL for the instance you were given.  

## Table of content and resources

* [Workshop On YouTube](YOUTUBE LINK HERE)
* [Presentation](PDF OF SLIDES HERE)
* [Discord chat](DISCORD LINK HERE)

| Title  | Description
|---|---|
| **1 - Getting Connected** | [Instructions](#1-Getting-Connected)  |
| **2 - Part 2** | [Instructions](#Part-2)  |
| **3 - Resources** | [Instructions](#Resources)  |

## 1. Getting Connected
**✅ Step 1a: The first step in the section.**

In your browser window, navigate to the url <YOURADDRESS>:3000 where your address is the one emailed to you before the session.
  
When you arrive at the webpage you should be greeted by something similar to this.
<img src="https://user-images.githubusercontent.com/1936716/107884421-a23fe180-6eba-11eb-96d2-4c703ccb1dcf.png" width=“700” />

Click in the `Terminal` menu from the top of the page and select new terminal as shown below
<img src="https://user-images.githubusercontent.com/1936716/107884506-09f62c80-6ebb-11eb-9f7b-42bdb3444cc1.png" width=“700” />

Once you have opened the terminal run
```bash
kubectl get nodes
```

*📃output*

```bash
NAME                        STATUS   ROLES    AGE   VERSION
learning-cluster-master     Ready    master   49m   v1.19.4
learning-cluster-worker-0   Ready    <none>   49m   v1.19.4
learning-cluster-worker-1   Ready    <none>   49m   v1.19.4
ubuntu@learning-cluster-master:~/workshop$ 
```
If you see the above output you are ready for the lab.

## 2. Part 2

**✅ Step 2a: The first step in the section.**
**✅ Step 2b: Second step in the section**

## 3. Resources
For further reading and labs go to 
[link name](URL) 


```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

```bash
helm repo add k8ssandra https://helm.k8ssandra.io/stable
helm repo update
```

```bash 
helm repo add traefik https://helm.traefik.io/traefik
helm repo update
helm install traefik traefik/traefik -f traefik.yaml
```

```bash
kubectl get pods --all-namespaces
wget https://openebs.github.io/charts/openebs-operator.yaml
kubectl apply -f openebs-operator.yaml
kubectl get pods --all-namespaces
kubectl get blockdevice -n openebs
kubectl label bd -n openebs BLOCKDEVICENAMEHERE openebs.io/block-device-tag=learning
kubectl label bd -n openebs BLOCKDEVICENAMEHERE openebs.io/block-device-tag=learning
kubectl apply -f local-device-sc.yaml
kubectl get sc local-device
wget https://openebs.github.io/charts/examples/local-device/local-device-pvc.yaml
kubectl apply -f local-device-pvc.yaml
```


```bash
kubectl get pvc local-device-pvc
kubectl get sc local-device
```




```bash
helm install -f k8ssandra.yaml k8ssandra k8ssandra/k8ssandra
```

```bash
kubectl get cassandradatacenters

kubectl describe CassandraDataCenter dc1
```



