import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("0.0.0.0", 5005)
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(4096)
    print("data from client: "+data.decode())
    message = input('number: ')
    sent = sock.sendto(message.encode(), address)
