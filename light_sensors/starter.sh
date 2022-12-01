#!/bin/bash
/etc/init.d/ssh start
cat /tmp/hostExtras >> /etc/hosts
cat /etc/hosts
echo
echo "----------------------"
echo "Sending Light Readings"
echo "----------------------"
echo
python /root/app/light_sensor.py
#bash
