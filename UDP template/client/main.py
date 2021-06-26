import socket, sys

server_address = ('127.0.0.1', 5005)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    MESSAGE = input('input:')
    sock.sendto(MESSAGE.encode(), server_address)
    data, addr = sock.recvfrom(1024)
    print("number from server: "+data.decode())
