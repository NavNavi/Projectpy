# Socket Program

import socket

s = socket.socket()
print('Socket created ')
s.bind(('localhost',9999))
s.listen(3)
print("Welcome to server !")

while True:
    ac,add = s.accept() # it gives you client socket and client address
    name = ac.recv(1024).decode()
    print("Connected with client ", add,name)

    ac.send(bytes('Sending msg from server !','utf-8'))

    ac.close()