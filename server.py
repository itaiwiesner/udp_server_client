from scapy import *
from scapy.layers.inet import UDP
from scapy.sendrecv import sniff


def filter_port(pkt):
    """ This function return True if the packet's destination port is valid """
    return UDP in pkt and 20000 <= pkt[UDP].dport <= 20256


length = sniff(count=1, lfilter=filter_port)[0].dport - 2000
msg = []
for _ in length:
    msg.append(chr(sniff(count=1, lfilter=filter_port)[0].dport - 2000))

for i in msg:
    print(i, end='')
