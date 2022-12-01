#!/bin/bash
/etc/init.d/ssh start
/etc/init.d/mysql start
for (( ; ; ))
do
    
    echo
    echo "-----------------"
    echo "DB Server Started"
    echo "-----------------"
    echo
    echo -n "IP: "
    cat /etc/hosts
    sleep 7
    clear
done
