import socket

def Main():
    host = '127.0.0.1'
    port = 4000

    soc = socket.socket()
    soc.connect((host,port))

    message = input("-> ")
    while message != 'q':
        soc.send(message.encode('utf-8'))
        data = soc.recv(1024).decode('utf-8')
        print("from server: " + data)
        message = input("-> ")
    soc.close()

if __name__ == "__main__":
    Main()
