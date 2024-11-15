#!/bin/bash

container_name="project-cast-ai-workbench"

if docker ps | grep -q "$container_name"; then
  echo "Container $container_name is running"
else
  echo "Container $container_name is not running!"
  echo "Please start the project environment using the [Start Environment] button in AI Workbench."
  exit 1
fi

docker exec -t $container_name /bin/bash -c "/project/code/scripts/init-llm.sh"

docker exec -t $container_name /bin/bash -c "/project/code/scripts/init-tts.sh"

echo "All Done. You can run the applications now in the AI Workbench."
