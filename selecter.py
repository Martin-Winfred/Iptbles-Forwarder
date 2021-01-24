import os
import subprocess
#set gloable Flag
UDP_FLAG=False
TCP_FLAG=False
#Get User's imput in ssh|terminal
Cons_input=str(input('Imput your String with [Source ip,Source Port,dest ip,destation port]\n:'))
#Check UDP or TCP forwording Select
Select=(input('UDP=1\nTCP=2\nALL=3\nInput the number\n:'))
if Select=='1':
    UDP_FLAG=True
elif Select=='2':
    TCP_FLAG=True
else:
    TCP_FLAG=True
    UDP_FLAG=True
##print(str(UDP_FLAG))
##print(TCP_FLAG)
#Seprate Inputed Data
Sourc_ip,Monitor_Port,Dest_ip,Dest_port=Cons_input.split(',')
#get Local ip 
# Bash ip address check command: [ip -4 addr | grep -v 127.0.0.1|grep -oP '(?<=inet\s)\d+(\.\d+){3}']
local_ip_get=os.popen("ip -4 addr | grep -v 127.0.0.1|grep -oP '(?<=inet\s)\d+(\.\d+){3}'")
local_ip=str(local_ip_get.read())
print(local_ip)
'''
iptables -t nat -A PREROUTING -p tcp -m tcp --dport [源端口号] -j DNAT --to-destination [目标IP:目标端口号]
iptables -t nat -A PREROUTING -p udp --dport [源端口号] -j DNAT --to-destination [目标IP:目标端口号]
iptables -t nat -A POSTROUTING -p tcp -m tcp -dport [目标IP] --dport [目标端口号] -j SNAT --to-source [中转服务器IP]
iptables -t nat -A POSTROUTING -p udp  -m tcp -dport [目标IP] --dport [目标端口号] -j SNAT --to-source [中转服务器IP]


iptables -t nat -A PREROUTING -p tcp --dport $localport -j DNAT --to-destination $remote:$remoteport
iptables -t nat -A PREROUTING -p udp --dport $localport -j DNAT --to-destination $remote:$remoteport
iptables -t nat -A POSTROUTING -p tcp -d $remote --dport $remoteport -j SNAT --to-source $local
iptables -t nat -A POSTROUTING -p udp -d $remote --dport $remoteport -j SNAT --to-source $local
'''
##print(os.system("iptables --help"))
#Use if to check the tcp/udp choise and use os.system to print 
if UDP_FLAG==True and TCP_FLAG==False:
    print("iptables -t nat -A PREROUTING -p udp --dport "+Monitor_Port+" -j DNAT --to-destination "+Dest_ip+":"+Dest_port)
    print("iptables -t nat -A POSTROUTING -p udp -d "+Dest_ip+" --dport "+Dest_port+" -j SNAT --to-source "+local_ip)

    print(os.system("iptables -t nat -A PREROUTING -p udp --dport "+Monitor_Port+" -j DNAT --to-destination "+Dest_ip+":"+Dest_port))
    print(os.system("iptables -t nat -A POSTROUTING -p udp -d "+Dest_ip+" --dport "+Dest_port+" -j SNAT --to-source "+local_ip))
elif TCP_FLAG==True and UDP_FLAG==False:
    print("iptables -t nat -A PREROUTING -p tcp --dport "+Monitor_Port+" -j DNAT --to-destination "+Dest_ip+":"+Dest_port)
    print("iptables -t nat -A POSTROUTING -p tcp -d "+Dest_ip+" --dport "+Dest_port+" -j SNAT --to-source "+local_ip)

    print(os.system("iptables -t nat -A PREROUTING -p tcp --dport "+Monitor_Port+" -j DNAT --to-destination "+Dest_ip+":"+Dest_port))
    print(os.system("iptables -t nat -A POSTROUTING -p tcp -d "+Dest_ip+" --dport "+Dest_port+" -j SNAT --to-source "+local_ip))
else:
    print("iptables -t nat -A PREROUTING -p udp --dport "+Monitor_Port+" -j DNAT --to-destination "+Dest_ip+":"+Dest_port)
    print("iptables -t nat -A POSTROUTING -p udp -d "+Dest_ip+" --dport "+Dest_port+" -j SNAT --to-source "+local_ip)
    print("iptables -t nat -A PREROUTING -p tcp --dport "+Monitor_Port+" -j DNAT --to-destination "+Dest_ip+":"+Dest_port)
    print("iptables -t nat -A POSTROUTING -p tcp -d "+Dest_ip+" --dport "+Dest_port+" -j SNAT --to-source "+local_ip)

    print(os.system("iptables -t nat -A PREROUTING -p udp --dport "+Monitor_Port+" -j DNAT --to-destination "+Dest_ip+":"+Dest_port))
    print(os.system("iptables -t nat -A POSTROUTING -p udp -d "+Dest_ip+" --dport "+Dest_port+" -j SNAT --to-source "+local_ip))
    print(os.system("iptables -t nat -A PREROUTING -p tcp --dport "+Monitor_Port+" -j DNAT --to-destination "+Dest_ip+":"+Dest_port))
    print(os.system("iptables -t nat -A POSTROUTING -p tcp -d "+Dest_ip+" --dport "+Dest_port+" -j SNAT --to-source "+local_ip))
