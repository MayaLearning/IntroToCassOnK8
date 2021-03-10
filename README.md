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
| **2 - Setting Up Storage** | [Instructions](#Setting-Up-Storage)  |
| **3 - Setting Up Cassandra** | [Instructions](#Setting-Up-Cassandra)  |
| **4 - Connecting To Cassandra** | [Instructions](#Connecting-To-Cassandra)  |
| **5 - Resources** | [Instructions](#Resources)  |

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

## 2. Setting Up Storage

**✅ Step 2a: Setting Up Block Devices.**
```bash
kubectl get pods --all-namespaces
```

```bash
wget https://openebs.github.io/charts/openebs-operator.yaml
kubectl apply -f openebs-operator.yaml
kubectl get pods --all-namespaces
```

```bash
kubectl get blockdevice -n openebs
kubectl label bd -n openebs BLOCKDEVICENAMEHERE openebs.io/block-device-tag=learning
kubectl label bd -n openebs BLOCKDEVICENAMEHERE openebs.io/block-device-tag=learning
```

```bash
kubectl apply -f local-device-sc.yaml
kubectl get sc local-device
```


**✅ Step 2b: Setting Up PVC.**
```bash
wget https://openebs.github.io/charts/examples/local-device/local-device-pvc.yaml
kubectl apply -f local-device-pvc.yaml
```


**✅ Step 2b: Verify Config**

```bash
kubectl get pvc local-device-pvc
kubectl get sc local-device
```

## 3. Setting Up Cassandra

**✅ Step 3a: Install Helm**
```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

**✅ Step 3b: Add the K8ssandra repo**
```bash
helm repo add k8ssandra https://helm.k8ssandra.io/stable
helm repo update
```

**✅ Step 3c: Setup the Ingress**
```bash 
helm repo add traefik https://helm.traefik.io/traefik
helm repo update
helm install traefik traefik/traefik -f traefik.yaml
```

**✅ Step 3d: configure the k8ssandra.yaml**
Open the file in the browser and add in your IP address where it says <YOURADDRESS>
  

**✅ Step 3e: Install the Cassandra Cluster**
```bash
helm install -f k8ssandra.yaml k8ssandra k8ssandra/k8ssandra
```

```bash
kubectl get cassandradatacenters

kubectl describe CassandraDataCenter dc1
```

## 4. Connecting To Cassandra

**✅ Step 4a: Retreave the Cluster username**
```bash
kubectl get secret k8ssandra-superuser -o jsonpath="{.data.username}" | base64 --decode
```

**✅ Step 4b: Retreave the Cluster password**
```bash
kubectl get secret k8ssandra-superuser -o jsonpath="{.data.password}" | base64 --decode
```

**✅ Step 4c: Install the Cassandra driver**

```bash
sudo pip3 install cassandra-driver
```

**✅ Step 4d: Setting Up Our CRUD**



## 5. Resources
For further reading and labs go to 
[link name](URL) 
