import asyncio
port = 12345
class CounterUDPServer:
    def __init__(self ,trackerDB,logger):
        self.counter = 0
        self.trackerDB = trackerDB
        self.logger = logger

    async def send_counter(self, data , addr):
        msg_list = data.decode().replace('\n','').split(' ')

        if msg_list[0] == '1':
            self.logger.log(f'user {msg_list[1]} is connected')
            self.trackerDB.add_online_user(msg_list[1])
            self.trackerDB.update_user(msg_list[1],(addr[0],msg_list[2]))

        elif msg_list[0] == '2':
            self.logger.log(f'user {msg_list[1]} disconnected')
            self.trackerDB.delete_online_user(msg_list[1])

        elif msg_list[0] == '3':
            self.logger.log(f'user {msg_list[1]} requested the address of the peers having the file {msg_list[2]}')
            addrs = self.trackerDB.find_seeder(msg_list[2])
            ad = '@'.join(i for i in addrs)
            self.logger.log(f'users {self.trackerDB.files[msg_list[2]]} had the file {msg_list[2]}')
            self.transport.sendto(ad.encode(),addr)
            self.logger.add_logs2file(msg_list[2],
                                      f'user {msg_list[1]} requested the address of the peers having the file {msg_list[2]}')

        elif msg_list[0] == '4':
            self.logger.log(f'user {msg_list[1]} get the {msg_list[2]} file successfully on port {msg_list[3]}')
            self.trackerDB.add_seeder(msg_list[1],msg_list[2])
            self.logger.add_logs2file(msg_list[2],
                                      f'user {msg_list[1]}  get {msg_list[2]} file on port {msg_list[3]}')


        elif msg_list[0] == '5':
            self.logger.log(f'user {msg_list[1]} shares the {msg_list[2]} file in the network')
            self.trackerDB.add_file(msg_list[2])
            self.trackerDB.add_seeder(msg_list[1],msg_list[2])
            self.logger.add_logs2file(msg_list[2],
                                       f'user {msg_list[1]} shares the {msg_list[2]} file in the network')

        elif msg_list[0] == '6':
            self.logger.log(f'user {msg_list[1]} failed to get {msg_list[2]} file on port {msg_list[3]}')
            self.logger.add_logs2file(msg_list[2],f'user {msg_list[1]} failed to get {msg_list[2]} file on port {msg_list[3]}')
        else:
            self.logger.log(f'user has send some thing wierd')
            self.transport.sendto('what!!!'.encode(), addr)
        self.logger.update_files(self.trackerDB.files)


    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        print(f"got {data.decode()} from {addr}")
        loop = asyncio.get_event_loop()
        loop.create_task(self.send_counter(data,addr))