Initial Commit


# Deployment of zookeeper, hdfs and kafka

## Operators

To add operators using helm, first add the helm repo:

```bash
helm repo add stackable-stable https://repo.stackable.tech/repository/helm-stable/
```

Next, add required operators to the namspace called `stackable`. If namespace `stackable` does not exist, create it using

```bash
kubectl create namespace stackable
```

Next run:

```bash
helm install -n stackable --wait zookeeper-operator stackable-stable/zookeeper-operator --version 23.7.0
helm install -n stackable --wait hdfs-operator stackable-stable/hdfs-operator --version 23.7.0
helm install -n stackable --wait commons-operator stackable-stable/commons-operator --version 23.7.0
helm install -n stackable --wait secret-operator stackable-stable/secret-operator --version 23.7.0
```

## Zookeeper

To setup a zookeeper cluster, use the files in `./k8sDeploymentFiles/zookeeper`

First, create a namespace called `zookeeper` using 
```bash
kubectl create namespace zookeeper
```

Next, run 
```bash
kubectl apply -n zookeeper -f zookeeper/zk.yml
kubectl apply -n zookeeper -f zookeeper/znode.yml
```

## Hdfs

To setup hdfs, we will be using the same namespace `zookeeper`

To deploy the hdfs system, run:
```bash
kubectl apply -n zookeeper -f hdfs/hdfs.yaml
```

## Kafka

To deploy kafka, first create at namespace called `kafka` using:

```bash
kubectl create namespace kafka
```

Next, setup required operator using:
```bash
helm install -n kafka strimzi-cluster-operator oci://quay.io/strimzi-helm/strimzi-kafka-operator --set watchAnyNamespace=true
```

Afterwards, run these commands to setup a kafka cluster and kafka tooling
```bash
kubectl apply -n kafka -f kafka/kafka.yaml
kubectl apply -n kafka -f kafka/kafka-extra.yaml
```