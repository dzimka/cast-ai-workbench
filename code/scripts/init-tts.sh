#!/bin/bash

# TTS: SunoAI/Bark
echo "Initializing TTS with ${CAST_AI_TTS_MODEL}"
python3 -c "from transformers import BarkModel; model = BarkModel.from_pretrained('${CAST_AI_TTS_MODEL}')"
echo "Done"

start_tts() {
  echo -n "Starting TTS server..."
  /home/workbench/.local/bin/fastapi run code/tts-server/app.py &
  echo "done"
}

is_tts_running() {
  curl -f http://localhost:8000/health > /dev/null 2>&1
  return $?
}

if ! is_tts_running; then
  start_tts
fi

start_attempts=0
max_attempts=60

echo "Waiting for TTS server to respond..."
while ! is_tts_running && (( start_attempts < max_attempts )); do
echo -n "o"
  sleep 1
  start_attempts=$((start_attempts+1))
done
echo ""

if ! is_tts_running; then
  echo "TTS server failed to start or is not responding after $max_attempts attempts"
  exit 1
fi

echo "TTS server is running."
