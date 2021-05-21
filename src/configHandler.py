import configparser
import os


class configHandle:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def rewriteCfg(self):
        self.config['private'] = {'token':'<replace this with your token>'}
        cfgfile = open(r".\secrets\config.cfg","w")
        self.config.write(cfgfile)
        cfgfile.close()
        return 0
        

    def loadCfg(self):
        if  os.path.exists(r".\secrets\config.cfg"):
            self.config.read(r".\secrets\config.cfg")
            return self.config
        else:
            return self.rewriteCfg()

    

if __name__ == "__main__":

    print("What do you want to do?")
    print("[1] - load config")
    print("[2] - rewrite config")
    question = input("input:")
    if question == '1':
        cfg = configHandle().loadCfg()
        if cfg == 0:
            print("Config file didn't exist, it had to be rewrited")
            print("paste your token inside the config file")
        else:
            print("token:",cfg['private']['token'])
    elif question == '2':
        cfg = configHandle().rewriteCfg()
        print("Config file got rewirted")
        print("paste your token inside the config file")

