#!/bin/bash
/etc/init.d/ssh start
/etc/init.d/apache2 start
service mosquitto start
for (( ; ; ))
do
    
    echo
    echo "-------------------------"
    echo "Mosquitto Server Started"
    echo "-------------------------"
    echo
    /root/monitor.py
    sleep 3
    clear
done
