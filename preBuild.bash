#!/bin/bash
# This file contains bash commands that will be executed at the beginning of the container build process,
# before any system packages or programming language specific package have been installed.
#
# Note: This file may be removed if you don't need to use it

apt-get update

pip install --upgrade pip

# curl -LsSf https://astral.sh/uv/install.sh | sh
# source $HOME/.local/bin/env
# uv pip install --system -r requirements.txt