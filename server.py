from scapy import *
from scapy.layers.inet import UDP
from scapy.sendrecv import sniff


def filter_port(pkt):
    """ This function return True if the packet's destination port is valid """
    return UDP in pkt and 20000 <= pkt[UDP].dport <= 20256


length = sniff(count=1, lfilter=filter_port)[0].dport - 20000
msg = []
for _ in range(length):
    char = sniff(count=1, lfilter=filter_port, timeout=1)
    if len(char) == 0:
        break
    msg.append(chr(char[0][UDP].dport - 20000))

for i in msg:
    print(i, end='')
