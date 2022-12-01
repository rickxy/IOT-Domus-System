#!/bin/bash
/etc/init.d/ssh start
cat /tmp/hostExtras >> /etc/hosts
echo
echo "----------------"
echo "   Interface"
echo "----------------"
echo
echo "Not fully implemented"
echo
python /root/app/interface.py
#bash
