#!/usr/bin/env python3

import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('New connection from '  + addr[0])

def fib(x):
    if x == 0:
    	return 0	
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

while True:
	data = conn.recv(1024)
	udata = int(data.decode('utf-8'))
	d = fib(udata)
	if not data:
		break
	conn.send(str(d).encode('utf-8'))

conn.close()

