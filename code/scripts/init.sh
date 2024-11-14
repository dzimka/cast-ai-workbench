#!/bin/bash

# git pull dzimka...

source variables.env
IMAGE_NAME=cast-ai-wb

# pre-fetch the required models
# LLM: llama3.2:1b
# ollama pull $CAST_AI_LLM_MODEL

# TTS: SunoAI/Bark
docker run --rm -it \
    -e HF_HOME=$HF_HOME-e CAST_AI_TTS_MODEL=$CAST_AI_TTS_MODEL \
    -v $(path):/project \
    $IMAGE_NAME \
    python3 -c "from transformers import BarkModel; model = BarkModel.from_pretrained('$CAST_AI_TTS_MODEL')"
