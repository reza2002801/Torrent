import socket
class TCPClient:
    def __init__(self,addr,buffSize):
        self.socket = socket.socket()
        self.addr = addr
        self.bufferSize = buffSize
    def connect(self):
        self.socket.connect(self.addr)
        self.socket.send('ack'.encode())
        print(self.socket.recv(self.bufferSize).decode())

    def send_message(self,  msg):

        self.socket.send(msg.encode())
        return self.socket.recv(self.bufferSize).decode()

    def close_connection(self):
        self.socket.close()