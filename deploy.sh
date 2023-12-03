#!/bin/bash

# SSH into Raspberry Pi and navigate to the target directory
ssh -t pi@192.168.0.42 "cd /home/pi/homestation && \

# Perform a git pull to update the repository
git pull && \

# build docker image
docker build --tag homestation-docker . && \

# Stop all running containers
docker ps -aq | xargs docker stop | xargs docker rm

# Run the docker image
docker run -d -p 8000:5000 homestation-docker

# Reboot the Raspberry Pi
sudo reboot"
