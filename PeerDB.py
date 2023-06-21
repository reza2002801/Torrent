import os
import pickle
class PeerDB:
    def __init__(self, id):
        self.addr1 = '/home/reza/PycharmProjects/Torrent/PeerDB/'+ str(id)+'/'

    def get_file(self,fileName):

        s = self.addr1+fileName
        print(s)
        try:
            with open(s, 'rb') as file:
                data = file.read()
                print(data)
            return data
        except:
            print('No such file exist!!!')
            return

    def save_file(self,fileName,data):
        with open(self.addr1+fileName, "wb") as text_file:
            text_file.write(data)

    def file_size(self,filename):
        return os.path.getsize(self.addr1+filename)