import socket, sys, random
from threading import Thread

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("0.0.0.0", 5005)
sock.bind(server_address)


def f(strPORT, IP):
    csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_address = (IP, int(strPORT))
    csock.bind(client_address)

    message = "NO"
    while message == "NO":
        data, address = csock.recvfrom(1024)
        nr = int(data.decode())
        print("From client on port "+str(i)+": "+data.decode())
        if nr == x:
            message = "YES"
        csock.sendto(message.encode(), address)
    csock.close()


x = random.randint(0, 100000)
print("X is: "+str(x))

i = 10000
while True:
    i += 1
    Data, Address = sock.recvfrom(1024)
    sock.sendto(str(i).encode(), Address)
    strPORT = str(i)
    t = Thread(target=f, args=(strPORT, Address[0]))
    t.start()
