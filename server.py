import socket
s = socket.socket()
s.bind((socket.gethostname(),8880))
s.listen(4)

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established! ")
    clientsocket.send(bytes("welcome to the server!","utf-8"))
    clientsocket.close()
