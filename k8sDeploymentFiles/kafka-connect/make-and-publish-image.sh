#!/bin/sh
tag=7.3.1
imagetag=kafka-connect
containername=cp-server-connect-base
dockerhubacc=hannehue
imagename=$dockerhubacc/$containername:$imagetag

echo $imagename
docker build --build-arg="CP_VERSION=$tag" --tag=$imagename  . 
# docker build --tag=$imagename  . 
# # docker run -it $imagename
# docker login -u hannehue --password-stdin
sudo docker login -u "hannehue" -p "Lsam4ZPgChBzKK2isb2fkoXL"
sudo docker push $imagename
