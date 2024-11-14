#!/bin/bash
# This file contains bash commands that will be executed at the end of the container build process,
# after all system packages and programming language specific package have been installed.
#
# Note: This file may be removed if you don't need to use it

# install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# pre-fetch the required models
# LLM: llama3.2:1b
ollama pull $CAST_AI_LLM_MODEL

# TTS: SunoAI/Bark
python3 -c "from transformers import BarkModel;model = BarkModel.from_pretrained('suno/bark-small')"

# add data folder
# sudo -E mkdir -p /data
# sudo -E chown workbench:workbench /data
