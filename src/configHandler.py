import configparser
import os
import pickle


class fileHandler:
    #def __init__(self):
        
    def rewriteCfg(self):
        self.config['private'] = {'token':'<replace this with your token>'}
        cfgfile = open(r".\data\config.cfg","w")
        self.config.write(cfgfile)
        cfgfile.close()
        return 0
        

    def loadCfg(self):
        if  os.path.exists(r".\data\config.cfg"):
            self.config.read(r".\data\config.cfg")
            return self.config
        else:
            return self.rewriteCfg()
    
    def loadData(self):
        file_location = r".\data\serverdata.data"
        if os.path.exists(file_location):
            with open(file_location):
                dataFile = pickle.load(file_location)
            return dataFile
        else:
            datafile = {}
            return datafile
            
        #TODO
        return 0

    def saveData(self, server_data):
        file_location = r".\data\serverdata.data"
        with open(file_location, "w"):
            pickle.dump(server_data, file_location)

        #TODO
        return 0



    

if __name__ == "__main__":

    print("What do you want to do?")
    print("[1] - load config")
    print("[2] - rewrite config")
    question = input("input:")
    if question == '1':
        cfg = fileHandler().loadCfg()
        if cfg == 0:
            print("Config file didn't exist, it had to be rewrited")
            print("paste your token inside the config file")
        else:
            print("token:",cfg['private']['token'])
    elif question == '2':
        cfg = fileHandler().rewriteCfg()
        print("Config file got rewirted")
        print("paste your token inside the config file")

