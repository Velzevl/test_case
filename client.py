import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
b = bytes(input('Vvedite chislo '), encoding = 'utf-8')
sock.send(b)

data = sock.recv(1024)
sock.close()

print(data.decode("utf-8"))