# syntax=docker/dockerfile:1

FROM arm32v6/python:3.7.10-alpine3.13

WORKDIR /homestation-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]



