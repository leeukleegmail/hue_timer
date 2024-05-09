CONTAINER_NAME="hue_fish_timer"

ON_TIME="11:00"
ON_DURATION="7"


CO2_SOCKET=19
BRIDGE_IP="192.168.178.158"
SCRIPT_NAME="fish.py"

docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker build --tag $CONTAINER_NAME --build-arg container_name=$CONTAINER_NAME .
docker run -d --name $CONTAINER_NAME --env ON_TIME=$ON_TIME --env ON_DURATION=$ON_DURATION --env CO2_SOCKET=$CO2_SOCKET --env BRIDGE_IP=$BRIDGE_IP --env SCRIPT_NAME=$SCRIPT_NAME --restart unless-stopped -v $(pwd)/:/$CONTAINER_NAME $CONTAINER_NAME

