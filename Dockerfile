# syntax=docker/dockerfile:1

FROM hypriot/rpi-python:3.7-slim

WORKDIR /homestation-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]



