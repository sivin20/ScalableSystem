docker build -t producer .

docker tag producer:latest sivin20/pythonproducer

docker push sivin20/pythonproducer