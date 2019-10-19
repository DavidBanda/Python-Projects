import socket

server = 'www.pythonprogramming.com'
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def pScan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, port))
        return True
    except:
        return False

for x in range(1, 65535):
    if pScan(x):
        print('Port:',x,'is open!!!!!!!!!!!!')
    else:
        '''print('Port',x,'is closed')'''
