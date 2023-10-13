CONTAINER_NAME="hue_timer"
ON_TIME="09:30"
OFF_TIME="20:00"
LIGHT_NUMBER=18
BRIDGE_IP="192.168.1.10"

docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker build --tag $CONTAINER_NAME --build-arg container_name=$CONTAINER_NAME .
docker run -d --name $CONTAINER_NAME --env ON_TIME=$ON_TIME --env OFF_TIME=$OFF_TIME --env LIGHT_NUMBER=$LIGHT_NUMBER --env BRIDGE_IP=$BRIDGE_IP --restart unless-stopped -v $(pwd)/:/$CONTAINER_NAME $CONTAINER_NAME

