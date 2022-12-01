FROM ubuntu:bionic
#RUN ls
RUN apt update
RUN apt-get update
RUN apt-get -y install netcat
RUN apt-get -y install e3
RUN apt-get -y install net-tools
RUN apt-get -y install openssh-server sudo
RUN apt-get -y install man
RUN apt-get -y install iputils-ping

RUN sudo apt-get -y install mosquitto mosquitto-dev mosquitto-clients 

RUN apt-get -y install nmap python-pip
RUN pip install paho-mqtt

COPY starter.sh /root/

COPY app/ /root/app


RUN chmod u+x /root/starter.sh
COPY hostExtras /tmp/hostExtras
RUN mkdir /root/.ssh
COPY authorized_keys /root/.ssh/.

CMD ["/root/starter.sh"]
