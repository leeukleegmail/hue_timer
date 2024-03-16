CONTAINER_NAME="hue_light_timer"

GROUP_NAME="Sofa"
BRIDGE_IP="192.168.1.10"
SCRIPT_NAME="light.py"

docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker build --tag $CONTAINER_NAME --build-arg container_name=$CONTAINER_NAME .
docker run -d --name $CONTAINER_NAME --env GROUP_NAME=$GROUP_NAME --env BRIDGE_IP=$BRIDGE_IP --env SCRIPT_NAME=$SCRIPT_NAME --restart unless-stopped -v $(pwd)/:/$CONTAINER_NAME $CONTAINER_NAME

