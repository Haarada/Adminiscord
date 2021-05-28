



class ServerData:
    def __init__(self, server_id):

        try:
            server_id = int(server_id)

        except ValueError:
            print("[ERROR][ServerData] - server_id have to be integer type")
            return -1

        else:
            self.serverid = server_id
            self.user_list = {}
            self.ignoredroles = []

    # __init end ========
    
    def add_user(self, user_id):
        
        if user_id in self.user_warns.keys():
            print("[INFO][ServerData] - user was already added")
            return -1
        else:
            self.user_list[user_id] = {"autowarns":0, "manualwarns":0,"bans":0}
            return 0


class ServerList:
    def __init__(self):
        self.server_list = {}

    def add_server(self, server_id):

        try:
            server_id = int(server_id)

        except ValueError:
            print("[ERROR][ServerList] - server_id have to be integer type")
            return -1

        else:
            if server_id in self.server_list.keys():
                print("[INFO][ServerList] - Server was already added")
                return -1
            self.server_list[server_id] = ServerData(server_id)
            return 0
        




#serverlist = {1:ServerData(1), 2:ServerData(2), ...}

#userlist = {1:{}, 2:{}, ...}
