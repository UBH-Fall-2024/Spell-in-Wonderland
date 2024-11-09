FROM python:3.12

ENV HOME /root
WORKDIR /root

COPY . .

RUN pip3 install requirements.txt

EXPOSE 8000