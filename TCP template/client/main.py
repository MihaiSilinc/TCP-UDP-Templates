import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("0.0.0.0", 7777))
s.send(b"Salut")
print(s.recv(1024).decode())
s.close()
