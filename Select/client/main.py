import socket
import select
import sys

def run():
    try:
        connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection_socket.connect(("0.0.0.0", 12324))
    except socket.error as message:
        print(message.strerror)
        exit(-1)


    while True:
        readers, _, _ = select.select([sys.stdin, connection_socket], [], [])
        for reader in readers:
            if reader is connection_socket:  # if connection_socket is the one ready we receive from the server
                try:
                    message = connection_socket.recv(256).decode()
                    if message == "":
                        print("The server has shut down! The client will no disconnect")
                        exit(1)
                    print(message)
                except socket.error as message:
                    print(message.strerror)
                    connection_socket.close()
                    exit(-2)
            else:  # otherwise the client has typed something so we send it to the server
                try:
                    message = input()
                    print("Sending to server: ", message)
                    connection_socket.sendall(message.encode())
                except socket.error as message:
                    print(message.strerror)
                    connection_socket.close()
                    exit(-3)

    connection_socket.close()


run()
