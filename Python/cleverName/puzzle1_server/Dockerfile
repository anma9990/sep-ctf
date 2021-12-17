FROM ubuntu:latest
MAINTAINER Angus & James

RUN apt-get update
RUN apt-get install openssh-server sudo -y
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo python1
RUN echo 'python1:python1' | chpasswd
RUN service ssh start

WORKDIR /home/ubuntu
COPY server.py ./
COPY persistent_server.sh ./
RUN chmod +x persistent_server.sh

EXPOSE 22

RUN mkdir -p /home/ubuntu/ssh_cmd
WORKDIR /home/ubuntu/ssh_cmd
CMD ["/usr/sbin/sshd","-D"]
WORKDIR /home/ubuntu
CMD ["./persistent_server.sh","&"]
