#!/bin/bash

# SSH into Raspberry Pi and navigate to the target directory
ssh -t ioles@192.168.0.27 "cd /home/ioles/homestation && \

# Perform a git pull to update the repository
git pull && \

# build docker image
sudo docker build --tag homestation-docker . && \

# Stop all running containers
sudo docker ps -aq | xargs docker stop | xargs docker rm && \

# Run the docker image
sudo docker run -d -p 8000:5000 homestation-docker && \

# Reboot the Raspberry Pi
sudo reboot"
