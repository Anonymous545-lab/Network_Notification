from scapy.all import *

def send_notification(ip, message):
    packet = IP(dst=ip)/ICMP()/Raw(load=message)
    send(packet)

if __name__ == "__main__":
    send_notification('Your IP', 'This is a test notification.')
