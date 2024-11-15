ARG baseImage=bitnami/pytorch:latest

FROM ${baseImage}

WORKDIR /opt/project/build

# apt dependencies
COPY apt.txt .
RUN apt-get update && apt-get install -y $(cat apt.txt)

# install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# python dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# add project volume
VOLUME /project
WORKDIR /project

ENTRYPOINT ["/bin/sh", "-c", "sleep infinity"]
