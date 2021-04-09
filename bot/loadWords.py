import os

class loadWords:
    def __init__(self):
        self.words = ['empty']
        

    def lw(self):
        if  os.path.exists(r".\secrets\bannedwords.txt"):
            wfile = open(r".\secrets\bannedwords.txt","r")
            self.words = wfile.read().splitlines()
            wfile.close()
            return self.words
        else:
            return ["error"]


if __name__ == "__main__":
    words = loadWords().lw()
    print("loaded words:", words)