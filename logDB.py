import logging
class LogDB:
    def __init__(self,fileName):

        self.fileName = fileName
        self.loglist = []
        self.files =  None
        self.final = {}

    def log(self, message=None ):
        FORMAT = '%(asctime)s %(message)s'
        logging.basicConfig(format=FORMAT, filename=self.fileName)
        logging.warning(message)

    def  show_tracker_logs(self):
        with open(self.fileName) as f:
            f = f.readlines()

        for line in f:
            print(line)

    def update_files(self, files_seeder):
        self.files = files_seeder

    def log_file(self,fileName):
        if fileName in self.files.keys():
            print(self.files[fileName])
        else:
            print(f'{fileName} not found')
    def add_logs2file(self,fileName, logmsg):

        """adds the log message related to one specific file to its key in a dictionary"""

        if fileName not in self.files.keys():
            self.final[fileName].append(logmsg)
        else:
            self.final[fileName] = []
            self.final[fileName].append(logmsg)
    def logs_of_the_file(self,fileName):
        if fileName in self.files.keys() :
            print(self.files[fileName])
            if fileName in self.final.keys():
                print(self.final[fileName])
            else:
                print('No log yet')
        else:
            print(f'{fileName} not found')
    def all_logs(self):
        for fileName in self.files.keys():
            self.logs_of_the_file(fileName)



