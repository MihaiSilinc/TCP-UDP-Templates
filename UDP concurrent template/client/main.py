import socket, sys

server_address = ('127.0.0.1', 5005)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

connect_message = "connect"
sock.sendto(connect_message.encode(), server_address)
data, addr = sock.recvfrom(1024)
PORT = int(data.decode())

sock.close()
server_address = ('127.0.0.1', PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = ""
while data != "YES":
    MESSAGE = input('input:')
    sock.sendto(MESSAGE.encode(), server_address)
    data, addr = sock.recvfrom(1024)
    data = data.decode()
    print("number from server: "+data)
