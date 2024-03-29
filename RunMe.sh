#!/bin/bash
if [ $EUID -ne 0 ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

#!/bin/bash
#menu.sh
 
source ~/.bashrc
echo "----------------------------------"
echo "please enter your choise:"
echo "1) Run iptables forwording selecter"
echo "2) show all the iptable ruls"
echo "3) print all the ipv4 address this device has(no localhost shows)"
echo "4) Enable Forwarding function(Ipv4)"
echo "0) Exit Menu"
echo "----------------------------------"
read input
 
case $input in
    0)
    echo Bye
    sleep 1
    exit 1;;
    1)
    echo Here we go
    sleep 1
    python3 selecter.py;;
    2)
    echo Here are your rules
    sleep 1
    iptables -t nat -nvL --line-numbers;;
    3)
    echo Here are your ip addresses
    sleep 1
    ip -4 addr | grep -v 127.0.0.1|grep -oP '(?<=inet\s)\d+(\.\d+){3}';;
    4)
    echo The status wil not be Save after reboot
    sleep
    sysctl net.ipv4.ip_forward=1;;
esac
