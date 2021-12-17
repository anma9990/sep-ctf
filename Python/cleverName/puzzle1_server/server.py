import socket

hostname = socket.gethostname()
server_ip = socket.gethostbyname(hostname)

HOST = server_ip
PORT = 4444

s = socket.socket()
s.bind((HOST,PORT))
s.listen()
conn, addr = s.accept()

conn.send('Successfully connected to the host!\nIP: {}\nPORT: {}\nServer resets every 30 seconds\nWARNING: Empty strings close the socket (only hit enter after typing something)'.format(HOST,PORT).encode())
while True:
    raw = conn.recv(2048)
    msg = raw.decode()
    if (msg == "exit"):
        conn.send('ok bye'.encode())
        break
    elif (msg == "someSecret"):
        conn.send('70d80b4'.encode())
    else:
        conn.send('Incorrect'.encode())

conn.send('\nShutting down server...'.encode())        
conn.close()
