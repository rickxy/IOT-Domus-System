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
RUN apt-get -y install e3
# RUN useradd -ms /bin/bash admin
# RUN echo admin:jshdgfjusdf|chpasswd

RUN apt-get -y install apache2
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN apt-get -y install libapache2-mod-php
COPY monitor.py /root/
RUN chmod u+x /root/monitor.py
COPY starter.sh /root/
RUN chmod u+x /root/starter.sh
COPY web /var/www/html/
COPY authorized_keys /root/.ssh/.
RUN sed -i -e 's/AllowOverride None/AllowOverride All/g' /etc/apache2/apache2.conf
RUN sed -i -e 's/Require all denied/Require all granted/g' /etc/apache2/apache2.conf

CMD ["/root/starter.sh"]
