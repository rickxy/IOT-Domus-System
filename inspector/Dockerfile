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

RUN apt-get -y install tcpdump

RUN useradd -ms /bin/bash user
RUN echo user:resu|chpasswd
RUN mv /usr/sbin/tcpdump /bin/tcpdump
COPY starter.sh /root/
COPY hostExtras /tmp/hostExtras
RUN chmod u+x /root/starter.sh
CMD ["/root/starter.sh"]
