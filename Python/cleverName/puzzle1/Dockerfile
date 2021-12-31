FROM ubuntu:latest
MAINTAINER Angus & James

RUN apt-get update
RUN apt-get install openssh-server sudo gnupg -y
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo python1
RUN echo 'python1:python1' | chpasswd
RUN service ssh start

WORKDIR /home/ubuntu
RUN mkdir -p /home/ubuntu/hints
RUN mkdir -p /home/ubuntu/solutions
COPY ./solutions/0.py ./solutions
COPY ./solutions/1.py ./solutions
COPY ./solutions/2.py ./solutions
COPY ./hints/hint0.txt ./hints
COPY ./hints/hint1.txt ./hints
COPY ./hints/hint2.txt ./hints
COPY ./flag0.txt ./
COPY ./flag1.txt.gpg ./
COPY ./common_passwords.txt ./

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]
