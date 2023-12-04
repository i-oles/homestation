# syntax=docker/dockerfile:1

FROM balenalib/raspberry-pi-debian-python:latest

# Install build dependencies
RUN apt-get update && \
    apt-get install -y build-essential

WORKDIR /homestation-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]



