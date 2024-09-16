#!/bin/bash
# This file contains bash commands that will be executed at the end of the container build process,
# after all system packages and programming language specific package have been installed.
#
# Note: This file may be removed if you don't need to use it

# add data folder
sudo -E mkdir -p /data
sudo -E chown workbench:workbench /data

# Grant user sudo access
# echo "workbench ALL=(ALL) NOPASSWD:ALL" | \
#     sudo tee /etc/sudoers.d/00-workbench > /dev/null
