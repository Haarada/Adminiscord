import configparser
import os
import pickle


class fileHandler:
    def __init__(self):
        self.config_location = r".\data\config.cfg"
        self.serverdata_location = r".\data\serverdata.data"
        
    def rewriteCfg(self):
        self.config = configparser.ConfigParser()
        self.config['private'] = {'token':'<replace this with your token>', 'owner_id': '<replace this with your id>'}
        if os.path.exists(self.config_location):
            with open(self.config_location,"w") as cfgfile:
                self.config.write(cfgfile)
        else:
            with open(self.config_location,"x") as cfgfile:
                self.config.write(cfgfile)

        

        return 0
        

    def loadCfg(self):
        if  os.path.exists(self.config_location):
            self.config = configparser.ConfigParser()
            self.config.read(self.config_location)
            return self.config
        else:
            return self.rewriteCfg()
    
    def loadData(self):
        if os.path.exists(self.serverdata_location):
            with open(self.serverdata_location, "rb") as datafile:
                dataFile = pickle.load(datafile)
            return dataFile
        else:
            datafile = {}
            return datafile
            
        #TODO
        return 0

    def saveData(self, server_data):
        if os.path.exists(self.serverdata_location):
            with open(self.serverdata_location, "wb") as datafile:
                pickle.dump(server_data, datafile)
        else:
            with open(self.serverdata_location, "xb") as datafile:
                pickle.dump(server_data, datafile)


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

