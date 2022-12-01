#!/bin/bash
/etc/init.d/ssh start
cat /tmp/hostExtras >> /etc/hosts
cat /etc/hosts
echo
echo "---------------------"
echo "Sending Temp Readings"
echo "---------------------"
echo
python /root/app/temp_sensor.py
#bash
