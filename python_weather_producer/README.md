
How to -> Byg og push image til registry, og apply den til kubectl

Byg image først

```bash
docker build -t pythonproducer .
```

Push til registry:

Sørg for at være logged in på Sigurds Docker (Kun Sigurd kan push nyt image)
```bash
docker login

docker tag pythonproducer:latest sivin20/pythonproducer:latest

docker push sivin20/pythonproducer:latest
```

Apply til cluster

```bash
kubectl apply -f producer-deployment.yml 
```