#!/bin/bash
/etc/init.d/ssh start
cat /tmp/hostExtras >> /etc/hosts
echo "/bin/tcpdump -s0 -l -w pcap.pcap" > ~/.bash_history
echo "python -m SimpleHTTPServer" >> ~/.bash_history
echo
echo "---------"
echo "Inspector"
echo "---------"
echo
bash
