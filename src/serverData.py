



class ServerData:
    def __init__(self, server_id):

        try:
            # Data structure
            server_id = str(server_id)
            self.serverid = server_id
            self.user_list = {}

            # Additional settings
                # self.ignoredroles = []  # roles that are ignored by autowarn  -> discontinued 
            self.guildowner = 0
            self.ignoredusers = []
            self.autokick = 0      # automatically kicks when enabled (1) after 3 autowarns 

        except ValueError:
            print("[ERROR][ServerData] - server_id have to be str type")
            

    # __init end ========
    
    def add_user(self, user_id):
        
        if user_id in self.user_list.keys():
            print("[INFO][ServerData] - user was already added")
            return -1
        else:
            self.user_list[user_id] = {"autowarns":0, "manualwarns":0,"kicks":0}
            return 0

    def check_user(self, user_id):

        if user_id in self.user_list.keys():
            return 0
        else:
            return -1


class ServerList:
    def __init__(self):
        self.server_list = {}

    def add_server(self, server_id):

        try:
            #server_id = str(server_id)
            if server_id in self.server_list.keys():
                print("[INFO][ServerList] - Server was already added")
                return -1

            self.server_list[server_id] = ServerData(server_id)
            print("[INFO][ServerList] - Server was added succesfully")
            return 0

        except ValueError:
            print("[ERROR][ServerList] - server_id have to be int type")
            return -1
            
    
    def delete_server(self, server_id):

        try:
            #server_id = str(server_id)
            if server_id in self.server_list.keys():
                self.server_list.pop(server_id, None)
                return 0

            print("[INFO][ServerList] - There is no server with that ID")
            return -1

        except ValueError:
            print("[ERROR][ServerList] - server_id have to be int type")
            return -1

    def check_server(self, server_id):

        #server_id = str(server_id)
        if server_id in self.server_list.keys():
            return 0
        else:
            return -1
        




#serverlist = {1:ServerData(1), 2:ServerData(2), ...}
#userlist = {1:{}, 2:{}, ...}

# example:

# sl = ServerList()
# sl.add_server(123)
# sl.server_list[123].add_user(456)
# sl.server_list[123].user_list[456]["warns"]
