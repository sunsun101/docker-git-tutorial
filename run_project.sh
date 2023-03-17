#!/bin/bash

url="https://github.com/sunsun101/docker-git-tutorial.git"
repo_name="docker-git-tutorial"
docker_compose_file="docker-compose.yml"


if [ ! -d "$repo_name" ]; then
  git clone "$url"
  echo "Git repository cloned."
else
  echo "Git repository already exists."
fi

cd "$repo_name"

if [ ! -f "$docker_compose_file" ]; then
  echo "Docker Compose file does not exist."
  exit 1
fi

docker-compose up