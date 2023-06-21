import asyncio
import random
from threading import Thread

import asyncudp
import tqdm as tqdm

from Torrent.PeerDB import PeerDB
from Torrent.logDB import LogDB
from Torrent.tcpClient import TCPClient
from Torrent.tcpServer import TCPServer
from Torrent.udpClient import UDPClient
res = None
udpPort = 12345
logger = None
def get(port,file,id):
    global res
    global logger
    asyncio.run(send_udp_message(f'3 {str(id)} {str(file)}', answer=True))
    data, addr = res
    logger.log(f'the user on address {addr} have the file {file}')

    data = data.decode().split('@')
    data = random.choice(data).split(' ')

    dest_ip = int(data[1])

    # try:
    peerDB = PeerDB(id)
    tcpClient = TCPClient((data[0],dest_ip),2048)
    tcpClient.connect()
    filesize = tcpClient.send_message(file)
    filename = file
    print(filesize,'efdc',filename)
    progress = tqdm.tqdm(range(int(filesize)), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(peerDB.addr1+filename, "wb") as f:
        while True:

            bytes_read = tcpClient.socket.recv(4096)
            if not bytes_read:
                break

            f.write(bytes_read)

            progress.update(len(bytes_read))

    tcpClient.close_connection()
    asyncio.run(send_udp_message(f'4 {id} {file} {dest_ip}',False))

    logger.log(f'user {id} get the file {file} from the peer on address {addr}')
    # except:
    #     asyncio.run(send_udp_message(f'6 {id} {file} {dest_ip}', False))
    #     logger.log(f'user {id} failed to get the file  {file} from the peer on address {addr}')

async def run_client(message ,answer):
    sock = await asyncudp.create_socket(remote_addr=("127.0.0.1", udpPort))
    sock.sendto(message.encode())
    if answer:
        global res
        data,addr = (await sock.recvfrom())
        sock.close()
        return  (data,addr)
    sock.close()

async def send_udp_message(message ,answer ):
    task =asyncio.create_task(run_client(message ,answer))
    await task
    if answer:
        global res
        res = task.result()

    else:
        return



def quit1(id):
    asyncio.run(send_udp_message(f'2 {id}',False))

async def a(port, id):
    tcpServer = TCPServer(port, id)
    loop = asyncio.get_event_loop()
    loop.create_task(tcpServer.run_server())
def b(port,id):
    asyncio.run(a(port,id))
def share(id,file):
    global logger

    asyncio.run(send_udp_message(f'5 {id} {file}',False))
    logger.log(f'user {id} shares the file {file} on the network')
def main():
    print('Your Id: \n')
    id = int(input())
    print('Your Port: \n')
    port = int(input())
    global logger
    logger = LogDB(str(id)+'.log')

    thread = Thread(target=b, args=(port,id))
    thread.start()
    asyncio.run(send_udp_message(f'1 {id} {port}',False))
    logger.log(f'user {id} is online now')


    while True:
        print('Enter any command \n'
              ' share: share any file you want \n'
              ' get: get any file you want \n'
              ' q: quit the app'
              ' log: request logs'
              ' share: share a file  \n-----------------------------------------------------' )
        command = input()
        if command == 'get':
            get(port,input('enter the fileName:\n'),id)

        elif command == 'q':
            quit1(id)
            logger.log(f'user {id} is disconnected')
            break
        elif command == 'log':
            logger.show_tracker_logs()
        elif command == 'share':
            print('enter fileName:\n')
            fileName = input()
            share(id,fileName)
        else: print('I didnt undrestand!!!')

if __name__ == '__main__':
    main()