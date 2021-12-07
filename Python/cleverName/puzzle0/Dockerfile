FROM ubuntu:latest
MAINTAINER Angus & James

RUN apt-get update
RUN apt-get install openssh-server sudo -y
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo python0
RUN echo 'python0:python0' | chpasswd
RUN service ssh start

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]
