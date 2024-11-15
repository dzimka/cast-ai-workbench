#!/bin/bash

start_ollama() {
  echo -n "Starting Ollama..."
  ollama serve &> $OLLAMA_LOGS/ollama.log &
  echo "done"
}

is_ollama_running() {
  curl -f http://localhost:11434 > /dev/null 2>&1
  return $?
}

if ! is_ollama_running; then
  start_ollama
fi

start_attempts=0
max_attempts=60

echo "Waiting for Ollama server to respond..."
while ! is_ollama_running && (( start_attempts < max_attempts )); do
echo -n "o"
  sleep 1
  start_attempts=$((start_attempts+1))
done
echo ""

if ! is_ollama_running; then
  echo "Ollama failed to start or is not responding after $max_attempts attempts"
  exit 1
fi

echo "Ollama is running."

echo "Now pulling the models: ${CAST_AI_LLM_MODEL}"
ollama pull ${CAST_AI_LLM_MODEL}

echo "Done"

