import socket
import select

def run():
    sockets = []
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", 12324))
        server_socket.listen(5)
        sockets.append(server_socket)
    except socket.error as message:
        print(message.strerror)
        exit(-1)

    while True:
        readers, _, _ = select.select(sockets, [], [])
        for reader in readers:
            if reader is server_socket: # if the server_socket is the one ready we have a new connection
                try:
                    client_socket, _ = server_socket.accept()
                    sockets.append(client_socket)
                except socket.error as message:
                    print(message.strerror)
                    server_socket.close()
                    exit(-2)
            else: # otherwise we have to receive the data sent by a connected client
                try:
                    message = reader.recv(256).decode()
                    if message == "quit" or message == "": # the client has disconnected
                        reader.close()
                        sockets.remove(reader)
                        continue

                    print("Received from client {}: {}".format(reader.getpeername(), message))
                    for skt in sockets:
                        if skt != reader and skt != server_socket:
                            skt.sendall("Message from {}: {}".format(reader.getpeername(), message).encode())

                except socket.error as message:
                    print(message.strerror)
                    server_socket.close()
                    exit(-3)

    server_socket.close()


run()
