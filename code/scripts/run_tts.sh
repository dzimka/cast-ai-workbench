docker --context remote run -it --rm --gpus all --name cast-ai-tts \
    -v /ssd/apps/tts-server/models:/models \
    -p 8000:8000 tts-server
