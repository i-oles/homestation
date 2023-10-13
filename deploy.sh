#!/bin/bash

# SSH into Raspberry Pi and navigate to the target directory
ssh -t pi@192.168.0.42 "cd /home/pi/homestation && \

# Perform a git pull to update the repository
git pull && \

# Reboot the Raspberry Pi
python3 hs_app.py"