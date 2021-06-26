import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

message = b"a message"
while True:
    server.sendto(message, ("<broadcast>", 7777))
    print("message sent!\n")
    time.sleep(5)
