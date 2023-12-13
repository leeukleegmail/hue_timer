CONTAINER_NAME="hue_fish_timer"

ON_TIME="09:00"
ON_DURATION="10"
LIGHT_DELAY="1"
PAUSE_TIME="13:00"
PAUSE_DURATION="2"

LIGHT_SOCKET=20
CO2_SOCKET=19
BRIDGE_IP="192.168.1.10"
SCRIPT_NAME="fish.py"

docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker build --tag $CONTAINER_NAME --build-arg container_name=$CONTAINER_NAME .
docker run -d --name $CONTAINER_NAME --env ON_TIME=$ON_TIME --env ON_DURATION=$ON_DURATION --env LIGHT_DELAY=$LIGHT_DELAY --env CO2_SOCKET=$CO2_SOCKET --env PAUSE_TIME=$PAUSE_TIME --env PAUSE_DURATION=$PAUSE_DURATION --env LIGHT_SOCKET=$LIGHT_SOCKET --env BRIDGE_IP=$BRIDGE_IP --env SCRIPT_NAME=$SCRIPT_NAME --restart unless-stopped -v $(pwd)/:/$CONTAINER_NAME $CONTAINER_NAME

