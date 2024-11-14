ARG baseImage=bitnami/pytorch:latest

FROM ${baseImage}

WORKDIR /opt/project/build

# apt and pip dependencies
# COPY apt.txt .
# RUN apt-get update && apt-get install -y $(cat apt.txt)
RUN apt-get update && apt-get install -y curl wget

# install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

VOLUME /project
WORKDIR /project

ENTRYPOINT ["/bin/sh", "-c", "sleep infinity"]
