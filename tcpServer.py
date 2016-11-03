import socket

def Main():
    host = '127.0.0.1'
    port = 4000

    soc = socket.socket()
    soc.bind((host,port))

    soc.listen(1)
    c, addr = soc.accept()
    print("connection from: " + str(addr))
    while 1:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("from client: " + data)
        data = data.upper()
        print("sending back to client: " + data)
        c.send(data.encode('utf-8'))
    c.close()

if __name__ == '__main__':
    Main()
    
