docker --context remote run -it --rm --gpus all --name cast-ai-llm \
    -v /ssd/apps/llm-server:/ollama \
    -p 11434:11434 llm-server
