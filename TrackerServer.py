import asyncio
import pickle
from threading import Thread
from Torrent.TrackerDB import TrackerDB
from Torrent.logDB import LogDB
from Torrent.udpServer import CounterUDPServer
port = 12345
logger = LogDB('trackerlogs.log')
async def run_server():
    loop = asyncio.get_running_loop()
    global logger
    await loop.create_datagram_endpoint(
        lambda: CounterUDPServer(TrackerDB('../TrackerDB/files.txt','../TrackerDB/users.txt'),logger),
        local_addr=('127.0.0.1', port)
    )
    print(f"Listening on 127.0.0.1:{port}")
    while True:
        await asyncio.sleep(3600)

def Tracker_cli():
    global logger
    while True:
        print('-------------------------------\ncommands:\n log \n file_logs:file_name\nonline_users\n----------------------------')
        s = input()
        if s == 'log':
            logger.show_tracker_logs()
        elif s == 'file_logs':

            print('enter file_name')
            file_name = input()
            if file_name == 'all':
                logger.all_logs()
            else:
                logger.logs_of_the_file(file_name)
        elif s == 'online_users':
            pass
        else:
            print('I didnt undrestand')

def main():
    print('tracker started !!!!')
    thread = Thread(target=Tracker_cli, args=())
    thread.start()
    while True:
        asyncio.run(run_server())

if __name__ == '__main__':
    main()