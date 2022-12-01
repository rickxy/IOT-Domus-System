#!/bin/bash
/etc/init.d/ssh start
cat /etc/hosts
echo
echo "-------------"
echo "DOMUS Heating"
echo "-------------"
echo
echo "The system's intelligent, so you don't have to be..."
echo 
python /root/app/heat_control.py
#bash
