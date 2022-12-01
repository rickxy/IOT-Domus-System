#!/bin/bash
/etc/init.d/ssh start
cat /etc/hosts
echo
echo "-------------"
echo "DOMUS FAKE SENSOR"
echo "-------------"
echo
echo "The system's intelligent, so you don't have to be..."
echo 
python /root/app/fake_sensor.py
#bash
