import os
import socket
import asyncio
from threading import Thread

import tqdm as tqdm

from Torrent.PeerDB import PeerDB


class TCPServer:
    def __init__(self,port,id):
        self.peerDB = PeerDB(id)
        self.port = port
        self.id = id
        self.coroutines = []


    async def handle_client(self,client,addr):

        loop = asyncio.get_event_loop()
        request = (await loop.sock_recv(client, 2500)).decode()

        await loop.sock_sendall(client, 'seenack'.encode())
        request = (await loop.sock_recv(client, 2500)).decode()

        filesize = self.peerDB.file_size(request)


        await loop.sock_sendall(client, str(filesize).encode())

        filename = request
        progress = tqdm.tqdm(range(int(filesize)), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(self.peerDB.addr1+filename, "rb") as f:
            while True:
                bytes_read = f.read(4096)
                if not bytes_read:
                    break

                await loop.sock_sendall(client, bytes_read)

                progress.update(len(bytes_read))
        client.close()
    def b(self,client,addr):
        asyncio.run(self.handle_client(client,addr))
    async def run_server(self):

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', self.port))
        server.listen(8)


        loop = asyncio.get_event_loop()

        while True:
            client, addr = await loop.sock_accept(server)
            print("connected to client :",addr)
            thread = Thread(target=self.b, args=(client,addr))
            thread.start()

    def close_coroutines(self):
        for co in self.coroutines:
            co.close()

