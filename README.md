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

Next, run 
```bash
kubectl apply -n stackable -f zookeeper/zk.yml
kubectl apply -n stackable -f zookeeper/znode.yml
```

## Hdfs

To setup hdfs, we will be using the same namespace `zookeeper`

To deploy the hdfs system, run:
```bash
kubectl apply -n stackable -f hdfs/hdfs.yaml
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

## HBase Database

Stackable also has operators for HBase, so we will use those

If you have followed the previous steps, the helm repo should already be added, but in case it has been removed.
`helm repo add stackable-stable https://repo.stackable.tech/repository/helm-stable/`

First, follow the steps of installing Zookeeper and HDFS. When that has been done run
```
helm install -n stackable --wait listener-operator stackable-stable/listener-operator --version 23.11.0
helm install -n stackable --wait hbase-operator stackable-stable/hbase-operator --version 23.11.0
```

Once that is done, navigate to the `k8sDeploymentFiles/hbase` and run

`kubectl apply -n stackable -f zookeeper-hbase.yaml`

Next, setup the HBase cluster by running

`kubectl apply -n stackable -f hbase.yaml`


# Ja Hans, det er fint, men nu vil jeg gerne lave noget på det

Super, så skal du først ssh'e ind i én af vores vm'er

Enten 
* bds-g09-n0
* bds-g09-n1
* bds-g09-n2

Ved f.eks. 
`ssh bds-g09-n0`
Derved åbner du adgang til at port-forwarde ved kubectl

## Red Panda (Et ui til Kafka)

`kubectl port-forward svc/redpanda  8080:8080 -n kafka`

Navigér herefter til localhost:8080

## Kafka Schema Registry

`kubectl port-forward svc/kafka-schema-registry  8081:8081 -n kafka`
Her can du bruge cURL `curl localhost:8081` til at få dets data, eller blot navigere til localhost:8081

## Kafka Connect

`kubectl port-forward svc/kafka-connect  8083:8083 -n kafka`
Samme som Kafka Schema Registry `curl localhost:8083` eller blot navigere til localhost:8083

## ksqldb console

For at åbne ksqldb konsollen, kan du exec ind i containeren ved

`kubectl exec --namespace=kafka --stdin --tty deployment/kafka-ksqldb-cli -- ksql http://kafka-ksqldb-server:8088`

