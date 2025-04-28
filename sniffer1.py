import socket
import os

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
sniffer.bind(("YOUR_IPv4 ADDRESS", 0))
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print("Sniffing started... Press Ctrl+C to stop.")

try:
    while True:
        raw_data, addr = sniffer.recvfrom(65535)
        print(f"Packet received from {addr}: {raw_data[:50]}")
except KeyboardInterrupt:
    print("\nStopping sniffer.")

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
