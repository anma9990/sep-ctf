FROM ubuntu:latest
MAINTAINER Angus & James

RUN apt-get update
RUN apt-get install openssh-server sudo -y
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo python1
RUN echo 'python1:python1' | chpasswd
RUN service ssh start

WORKDIR /home/ubuntu
COPY client.py ./

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]
