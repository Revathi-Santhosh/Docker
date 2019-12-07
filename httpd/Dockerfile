FROM ubuntu:16.04

WORKDIR /usr/local/apache2

RUN mkdir -p /tmp/log/apache2

RUN apt-get update -y

RUN apt-get install apache2 -y

COPY envvars /etc/apache2/envvars

VOLUME /var/www /tmp/log/apache2 /etc/apache2

EXPOSE 80 443
