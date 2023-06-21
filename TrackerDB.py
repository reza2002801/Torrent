import pickle
class TrackerDB:
    def __init__(self,addr1,addr2):
        file1 = open(addr1, 'rb')
        self.addr_files = addr1
        self.files = pickle.load(file1)
        file1.close()

        file2 = open(addr2, 'rb')
        self.addr_users = addr2
        self.users = pickle.load(file2)
        file2.close()

        self.online_users = []
    def save(self):
        file1 = open(self.addr_files, 'wb')
        pickle.dump(self.files,file1)
        file1.close()

        file2 = open(self.addr_users, 'wb')
        pickle.dump(self.users, file2)
        file2.close()

    def __getitem__(self, item):
        return self.files[item]
    def add_file(self,file):
        if file not in self.files.keys():
            self.files[file] = []
        self.save()
    def add_seeder(self,seeder,file):
        self.files[file].append(seeder)
        self.save()
    def update_user(self,user , addr):
        self.users[user] = addr
        self.save()
    def add_online_user(self,user):
        self.online_users.append(user)
    def find_seeder(self,file):
        l = []
        for user in self.online_users:
            if user in self.files[file]:
                l.append(f'{self.users[str(user)][0]} {self.users[str(user)][1]}')

        return l

    def delete_online_user(self,user):
        self.online_users.remove(user)

