from socket import *
#import ssl

server = 'www.pythonprogramming.com'
#port = 443
port = 80
socket = socket(AF_INET, SOCK_STREAM)

#socket = ssl.wrap_socket(socket, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_TLS)
request = 'GET / HTTP/1.1\r\nHost: ' + server + '\r\n\r\n'

socket.connect((server, port))
#socket.sendall(query.encode())
socket.send(request.encode())
result = socket.recv(4096).decode()
#print(result)
#socket.close()

while(len(result) > 0):
    print(result)
    result = socket.recv(4096).decode()