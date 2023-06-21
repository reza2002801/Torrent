import asyncio

import asyncudp
class UDPClient:
    def __init__(self,port):
        asyncio.run(self.c(port))
    async def c(self,port):
        self.sock = await asyncudp.create_socket(remote_addr=("127.0.0.1", port))
    def send_message(self,msg):
        self.sock.sendto(msg)
    def recieve_message(self):
        return self.sock.recvfrom()
