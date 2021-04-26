# Intro to Cassandra On Kubernetes

##  Learning Workshop
In this session we will be taking a look at running a distributed system on top of another distributed system while using persistant storage to make sure our data stays in tact. 

## Before starting
Workshop attendees will be able to message Prasson in discord for a training instance.

Notice that training cloud instances will be available only during the workshop and will be terminated **24 hours later**. If you are in our workshop we recommend using the provided cloud instance, you can relax as we have you covered: prerequisites are installed already.

**⚡ IMPORTANT NOTE:**
Everywhere in this repo you see `<YOURADDRESS>` replace with the URL for the instance you were given.  

## Table of content 

| Title  | Description
|---|---|
| **1 - Getting Connected** | [Instructions](#1-Getting-Connected)  |
| **2 - Setting Up Storage** | [Instructions](#Setting-Up-Storage)  |
| **3 - Setting Up Cassandra** | [Instructions](#Setting-Up-Cassandra)  |
| **4 - Connecting To Cassandra** | [Instructions](#Connecting-To-Cassandra)  |
| **5 - Resources** | [Instructions](#Resources)  |

## 1. Getting Connected
**✅ Step 1a: The first step in the section.**

In your browser window, navigate to the url <YOURADDRESS>:3000 where your address is the one provided by Prasson.
  
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

Show the current pods that are running.

```bash
kubectl get pods --all-namespaces
```

*📃output*

```bash
NAMESPACE     NAME                                                READY   STATUS    RESTARTS   AGE
kube-system   coredns-f9fd979d6-pbs8m                             1/1     Running   0          10m
kube-system   coredns-f9fd979d6-wzcgn                             1/1     Running   0          10m
kube-system   etcd-learning-cluster-0-master                      1/1     Running   0          10m
kube-system   kube-apiserver-learning-cluster-0-master            1/1     Running   0          10m
kube-system   kube-controller-manager-learning-cluster-0-master   1/1     Running   0          10m
kube-system   kube-flannel-ds-cvjvp                               1/1     Running   0          3m
kube-system   kube-flannel-ds-xflrq                               1/1     Running   0          3m
kube-system   kube-flannel-ds-xw4m9                               1/1     Running   0          3m
kube-system   kube-proxy-9rzw4                                    1/1     Running   0          3m7s
kube-system   kube-proxy-jns28                                    1/1     Running   0          3m8s
kube-system   kube-proxy-mjgqj                                    1/1     Running   0          10m
kube-system   kube-scheduler-learning-cluster-0-master            1/1     Running   0          10m
```

Install OpenEBS

```bash
wget https://openebs.github.io/charts/openebs-operator.yaml
kubectl apply -f openebs-operator.yaml
kubectl get pods --all-namespaces
```

*📃output*

```bash
NAMESPACE     NAME                                                READY   STATUS              RESTARTS   AGE
kube-system   coredns-f9fd979d6-pbs8m                             1/1     Running             0          10m
kube-system   coredns-f9fd979d6-wzcgn                             1/1     Running             0          10m
kube-system   etcd-learning-cluster-0-master                      1/1     Running             0          11m
kube-system   kube-apiserver-learning-cluster-0-master            1/1     Running             0          11m
kube-system   kube-controller-manager-learning-cluster-0-master   1/1     Running             0          11m
kube-system   kube-flannel-ds-cvjvp                               1/1     Running             0          3m23s
kube-system   kube-flannel-ds-xflrq                               1/1     Running             0          3m23s
kube-system   kube-flannel-ds-xw4m9                               1/1     Running             0          3m23s
kube-system   kube-proxy-9rzw4                                    1/1     Running             0          3m30s
kube-system   kube-proxy-jns28                                    1/1     Running             0          3m31s
kube-system   kube-proxy-mjgqj                                    1/1     Running             0          10m
kube-system   kube-scheduler-learning-cluster-0-master            1/1     Running             0          11m
openebs       maya-apiserver-747fbf7f89-vgs86                     0/1     ContainerCreating   0          2s
openebs       openebs-admission-server-555b957648-dwls5           0/1     ContainerCreating   0          1s
openebs       openebs-localpv-provisioner-7d7c74fbbb-c78js        0/1     ContainerCreating   0          1s
openebs       openebs-ndm-4tcxw                                   0/1     ContainerCreating   0          1s
openebs       openebs-ndm-kbxdq                                   0/1     ContainerCreating   0          1s
openebs       openebs-ndm-operator-6bd5949967-66zw6               0/1     ContainerCreating   0          1s
openebs       openebs-provisioner-cd9474fb8-rvdj6                 0/1     ContainerCreating   0          2s
openebs       openebs-snapshot-operator-897d78956-2k8qq           0/2     ContainerCreating   0          2s
```

For each blockdevice listed you will need to add the learning tag so that it can be consumed as a resource by our pods. 

```bash
kubectl get blockdevice -n openebs
```

*📃output*

```bash
NAME                                           NODENAME                      SIZE          CLAIMSTATE   STATUS   AGE
blockdevice-6073c1a6970805a0c5f63b04dedb1f5b   learning-cluster-0-worker-0   75000000000   Unclaimed    Active   19s
blockdevice-6dcd4d6f4ff6be74c0b5fb0517244b53   learning-cluster-0-worker-1   75000000000   Unclaimed    Active   19s
```

```bash
kubectl label bd -n openebs BLOCKDEVICENAMEHERE openebs.io/block-device-tag=learning
kubectl label bd -n openebs BLOCKDEVICENAMEHERE openebs.io/block-device-tag=learning
```

*📃output*

```bash
blockdevice.openebs.io/blockdevice-6073c1a6970805a0c5f63b04dedb1f5b labeled
blockdevice.openebs.io/blockdevice-6dcd4d6f4ff6be74c0b5fb0517244b53 labeled
```

Setup the storage class.

```bash
kubectl apply -f local-device-sc.yaml
```

Verify storage class.


```bash
kubectl get sc local-device
```

*📃output*

```bash
NAME           PROVISIONER        RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-device   openebs.io/local   Delete          WaitForFirstConsumer   false                  1s
```


## 3. Setting Up Cassandra

**✅ Step 3a: Install Helm**
```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

*📃output*

```bash
Downloading https://get.helm.sh/helm-v3.5.3-linux-amd64.tar.gz
Verifying checksum... Done.
Preparing to install helm into /usr/local/bin
helm installed into /usr/local/bin/helm
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

*📃output*

```bash
NAME: traefik
LAST DEPLOYED: Mon Mar 15 15:54:45 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

**✅ Step 3d: configure the k8ssandra.yaml**

Open the file in the browser and add in your IP address where it says `<YOURADDRESS>`
  

**✅ Step 3e: Install the Cassandra Cluster**
```bash
helm install -f k8ssandra.yaml k8ssandra k8ssandra/k8ssandra
```


*📃output*

```bash
NAME: k8ssandra
LAST DEPLOYED: Mon Mar 15 15:55:46 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
```

```bash
kubectl get cassandradatacenters
```

*📃output*

```bash
NAME   AGE
dc1    98s
```

```bash
kubectl describe CassandraDataCenter dc1
```


*📃output*

```bash
Name:         dc1
Namespace:    default
Labels:       app.kubernetes.io/instance=k8ssandra
              app.kubernetes.io/managed-by=Helm
              app.kubernetes.io/name=k8ssandra
              app.kubernetes.io/part-of=k8ssandra-k8ssandra-default
              helm.sh/chart=k8ssandra-1.0.0
Annotations:  meta.helm.sh/release-name: k8ssandra
              meta.helm.sh/release-namespace: default
              reaper.cassandra-reaper.io/instance: k8ssandra-reaper
API Version:  cassandra.datastax.com/v1beta1
Kind:         CassandraDatacenter
...
Events:
  Type    Reason             Age                From           Message
  ----    ------             ----               ----           -------
  Normal  CreatedResource    95s                cass-operator  Created service k8ssandra-dc1-service
  Normal  CreatedResource    95s                cass-operator  Created service k8ssandra-seed-service
  Normal  CreatedResource    95s                cass-operator  Created service k8ssandra-dc1-all-pods-service
  Normal  CreatedResource    87s                cass-operator  Created statefulset k8ssandra-dc1-default-sts
  Normal  ScalingUpRack      87s (x2 over 87s)  cass-operator  Scaling up rack default
  Normal  LabeledPodAsSeed   31s                cass-operator  Labeled pod a seed node k8ssandra-dc1-default-sts-0
  Normal  StartingCassandra  26s                cass-operator  Starting Cassandra for pod k8ssandra-dc1-default-sts-0
```


## 4. Connecting To Cassandra

**✅ Step 4a: Retrieve the Cluster username**
```bash
kubectl get secret k8ssandra-superuser -o jsonpath="{.data.username}" | base64 --decode
```

Your output should look something like this.


*📃output*

```bash
k8ssandra-superuser
```


**✅ Step 4b: Retrieve the Cluster password**
```bash
kubectl get secret k8ssandra-superuser -o jsonpath="{.data.password}" | base64 --decode
```
Your output should look something like this.


*📃output*

```bash
xvKAjJ5CO9F2LOthC5GT
```

**✅ Step 4c: Testing our database**
```bash
kubectl exec --stdin --tty k8ssandra-dc1-default-sts-0 -- /bin/bash
cqlsh -u YOURUSERNAME -p YOURPASSWORD
```
This will bring you into the CQLSH prompt where you can directly interact with the database.
*📃output*

```bash
Connected to k8ssandra at 127.0.0.1:9042.
[cqlsh 5.0.1 | Cassandra 3.11.10 | CQL spec 3.4.4 | Native protocol v4]
Use HELP for help.
k8ssandra-superuser@cqlsh> 
```

**✅ Step 4d: Insert Data**
```bash
CREATE KEYSPACE test WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'dc1' : 3 };
CREATE TABLE test.users (username text, name text, age int, PRIMARY KEY(username));
INSERT INTO test.users(username,name,age) VALUES ('EricZ','Eric Zietlow',67);
SELECT * FROM test.users;
```

*📃output*

```bash
 username | age | name
----------+-----+--------------
    EricZ |  67 | Eric Zietlow
```

## 5. Resources
For further reading go to the [OpenEBS Docs](https://docs.openebs.io/) 

Check out our new Discord server [Invite](https://discord.gg/kkDTVQwJSN) 

Get into more with the Data On Kubernetes Community [DOKc](https://dok.community/)

For the K8ssandra Project [k8ssandra.io](k8ssandra.io)

Many more workshops to come so Please subscribe to the YouTube Channel to be notified. 
