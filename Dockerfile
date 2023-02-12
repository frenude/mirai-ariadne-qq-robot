FROM openjdk:11-jre

LABEL author.email="frenude@gmail.com"
LABEL version="1.0"

ENV TZ Asia/Shanghai
WORKDIR /app

ADD ./mcl-2.1.2.zip/ .

RUN unzip mcl-2.1.2.zip && \
    chmod +x mcl && \
    ./mcl --update-package net.mamoe:mirai-api-http --channel stable-v2 --type plugin &&\
    ./mcl --dry-run

EXPOSE 8080

CMD ["./mcl"]