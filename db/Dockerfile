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

# RUN useradd -ms /bin/bash admin
# RUN echo admin:vvjsdu733|chpasswd

# RUN apt-get -y install apache2

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server
RUN /etc/init.d/mysql start && mysqladmin -u root password eskiotrat
ENV MYSQL="mysql --defaults-file=/etc/mysql/debian.cnf"
COPY db_init.mysql /root/
ARG DB
ARG DB_USER
ARG DB_PASS
RUN echo  ${MYSQL} -e "CREATE DATABASE IF NOT EXISTS \`$DB\`;"
RUN /etc/init.d/mysql start && \
    ${MYSQL} -e "CREATE DATABASE IF NOT EXISTS \`$DB\`;" && \
    ${MYSQL} -e "GRANT ALL PRIVILEGES ON \`${DB}\`.* TO '${DB_USER}' IDENTIFIED BY '${DB_PASS}';"  && \
    ${MYSQL} --user=${DB_USER} --password=${DB_PASS} --database=$DB  < /root/db_init.mysql

RUN sed -e "s/^bind-address\(.*\)=.*/bind-address = 0.0.0.0/" -i /etc/mysql/mysql.conf.d/mysqld.cnf


RUN echo root:vvjsdu733|chpasswd
COPY starter.sh /root/
RUN chmod u+x /root/starter.sh
RUN mkdir /root/.ssh
COPY authorized_keys /root/.ssh/.
EXPOSE 3306/tcp
# COPY web /var/www/html/
CMD ["/root/starter.sh"]
