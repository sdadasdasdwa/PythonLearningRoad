from socket import *

host = '127.0.0.1'
port = 21567
bufsiz = 1024
addr = (host, port)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(addr)

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(bufsiz)
    if not data:
        print('no data')
        break
    print(data.decode('utf-8'))
tcpCliSock.close()