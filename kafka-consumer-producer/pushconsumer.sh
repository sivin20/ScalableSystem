docker build -t consumer -f Dockerfile-consumer .

docker tag consumer:latest sivin20/pythonconsumer

docker push sivin20/pythonconsumer