FROM python:3.12

ENV HOME /root
WORKDIR /root

COPY . .

# Download dependancies
RUN pip3 install -r requirements.txt

EXPOSE 8000
# It waits for other docker images to be started while using docker compose - from 312
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait

CMD /wait && python3 -u server.py