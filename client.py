from scapy import *
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import send

PORT = 20000
DEST_IP # this is the ip of the server
msg = input("enter your message: ")
# create and send a packet representing the length of the message
length_pkt = IP(dst=DEST_IP,) / UDP(sport=PORT, dport=len(msg) + 20000)
send(length_pkt)

for i in msg:
    pkt = IP(dst=DEST_IP,) / UDP(sport=PORT, dport=ord(i) + 20000)
    send(pkt)
