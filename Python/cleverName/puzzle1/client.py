import socket

HOST = '172.16.10.20' 
#'172.16.10.20'
PORT = 4444

s = socket.socket()
s.connect((HOST, PORT))

msg = s.recv(2048).decode()
print(msg)

while True:
    msg1 = input()
    s.sendall(msg1.encode())
    msg_inbound = s.recv(2048).decode()
    print(msg_inbound)
