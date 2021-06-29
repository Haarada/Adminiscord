from imports import *

settings = fH.fileHandler().loadCfg()
datafile = fH.fileHandler().loadData()
words = lW.loadWords().lw()
cmdprefix = "~~"

intents = discord.Intents.default()
#intents.members = True

client = commands.Bot(cmdprefix, intents=intents)



#   ========================================
#           On Ready event

@client.event
async def on_ready():

    print("Logged in as {0.user}".format(client))
    print("to stop bot write in the chat:", "STOP_"+client.user.discriminator)
    print("You have to be owner of the bot to do that.")
    print("Bot's prefix is:", cmdprefix)


#   ========================================
#           On message event

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # ==== \/ exiting the bot \/ ====
    if str(message.author.id) == str(settings['private']['owner_id']) and message.content == "STOP_"+client.user.discriminator:
        fH.fileHandler().saveData(datafile)
        print("Adminiscord is closing...")
        exit()


    # ==== \/ check if a message was sent in a server where data collecting is enabled \/ ====
    serverdata_check = datafile.check_server(message.guild.id) 
    if serverdata_check == 0:
        print("data is collected on",message.guild.id,"guild")
    else:
        print("data is NOT collected on",message.guild.id,"guild")



    msg = message.content
    # ==== \/ saving messages to file \/ ====

    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")    #   ISO 8601

    if  os.path.exists(".\\data\\messages\\"+str(message.guild.id)+".txt"):
        logchat = open(".\\data\\messages\\"+str(message.guild.id)+".txt","a")  # Open in Append mode
    else:
        logchat = open(".\\data\\messages\\"+str(message.guild.id)+".txt","x")  # open in Write mode (with file creation)
        
    logchat.write("["+time+"]["+message.channel.name+"]["+message.author.mention+"]["+msg+"]\n") 
    logchat.close()

    print("["+time+"]["+message.channel.name+"]["+message.author.display_name+"]["+msg+"]") # sending message to the console


    # ==== \/ "cesoring" messages \/ ====

    msg = msg.lower()
    deleteword = False
    for word in words:
        if word in msg:
            msg = msg.replace(word,"\*"*len(word))
            deleteword = True
            
    if deleteword == True:
        await message.channel.send(message.author.mention+" Watch your language! Censored message:\n> "+msg)
        await message.delete()
        #deleteword = False         Probably not required
    
    

    # ==== \/ if monitoring is enabled \/ ====

    if serverdata_check == 0:
        g_id = message.guild.id
        u_id = message.author.id

        if datafile.server_list[g_id].check_user(u_id) == -1:
            datafile.server_list[g_id].add_user(u_id)

        if datafile.server_list[g_id].autokick == 1:
            if deleteword and u_id not in datafile.server_list[g_id].ignoredusers: 
                datafile.server_list[g_id].user_list[u_id]['autowarns'] += 1
                
            if datafile.server_list[g_id].user_list[u_id]['autowarns'] >= 3:
                datafile.server_list[g_id].user_list[u_id]['autowarns'] = 0
                datafile.server_list[g_id].user_list[u_id]['kicks'] += 1
                await message.author.send("You have been kicked from the server, because you triggered auto-mod 3 times\n"\
                                            "To dispiute the kick, please write to the server owner <@!"+str(datafile.server_list[g_id].guildowner)+">")
                await message.author.kick(reason="You have triggered auto-mod 3 times")


    # ==== \/ function required to use discord commands ==== \/

    await client.process_commands(message)



#   ==========================================
#           Commands

# Template:

# @client.command()
# async def test(ctx, arg):
#     print("printing arg:", arg)
#     await ctx.send("printing arg: "+arg)

# @test.error
# async def test_err(ctx, error):
#     await ctx.send("You have to pass some arguments!")


# ==== \/ enabling data colletion on server \/ ====

@client.command()
async def serverdata(ctx, arg: str):   # typing module in "action"

    # permission check
    if (not ctx.message.author.guild_permissions.administrator):
        await ctx.send("You have to be server administrator to do that!")
        return -1

    if (arg.lower() == "enable"):
        test = datafile.add_server(ctx.guild.id)

        if test == 0:
            await ctx.send("Server added succesfully to the monitoring list")
            datafile.server_list[ctx.guild.id].guildowner = ctx.guild.owner_id
            return 0
        else:
            await ctx.send("Server is already on the monitoring list")
            return -1

    elif(arg.lower() == "disable"):
        test = datafile.delete_server(ctx.guild.id)
        if test == 0:
            await ctx.send("Server removed succesfully from the monitoring list. Data was removed and cannot be retrived")
            return 0
        else:
            await ctx.send("Server is not on the monitoring list")
            return -1

    else:
        #print("Invalid argument")
        raise ValueError

@serverdata.error
async def serverdata_err(ctx, error):
    await ctx.send("This function handles collecting user data: warns, kicks, etc.\n"\
                    "Function accepts two arguments:\n"\
                    "enable - to start collecting data\n"\
                    "disable - to disabling collecting data, and deleting previously collected data")


# =================================================


@client.command()
async def ignoreuser(ctx, mode, u_id):
    # permission check
    if (not ctx.message.author.guild_permissions.administrator):
        await ctx.send("You have to be server administrator to do that!")
        return -1

    serverdata_check = datafile.check_server(ctx.guild.id)
    if serverdata_check == -1:
        await ctx.send("This function requires data to be collected, to do that use:\n'~~serverdata enable'")
    else:
        if mode == "add":
            if u_id not in datafile.server_list[ctx.guild.id].ignoredusers:
                datafile.server_list[ctx.guild.id].ignoredusers.append(u_id)
                await ctx.send("User added to the ignored list")
                return 0
            else:
                await ctx.send("User is already in the ignored list")
                return -1

        elif mode == "remove":
            if u_id in datafile.server_list[ctx.guild.id].ignoredusers:
                datafile.server_list[ctx.guild.id].ignoredusers = [value for value in datafile.server_list[ctx.guild.id].ignoredusers if value != u_id]
                await ctx.send("User removed from the ignored list")
                return 0
            else:
                await ctx.send("There is no user with that ID in the ignored list")
                return -1
        else:
            raise ValueError

@ignoreuser.error
async def ignoreduser_err(ctx, error):
    await ctx.send("With this function you can add users to automod ignore list.\n"\
                    "Usage: '~~ignoreuser [add/remove] user_id'")


# ===============================================

@client.command()
async def autokick(ctx, arg: str):   # typing module in "action"

    # permission check
    if (not ctx.message.author.guild_permissions.administrator):
        await ctx.send("You have to be server administrator to do that!")
        return -1

    if (arg.lower() == "enable"):
        datafile.server_list[ctx.guild.id].autokick = 1
        await ctx.send("Autokick enabled on this server")
        return 0

    elif(arg.lower() == "disable"):
        datafile.server_list[ctx.guild.id].autokick = 0
        await ctx.send("Autokick disabled on this server")
        return -1

    else:
        #print("Invalid argument")
        raise ValueError

@autokick.error
async def autokick_err(ctx, error):
    await ctx.send("Autokicking when user gets 3 warnings\n"\
                    "Function usage: '~~autokick [enable/disable]'")
      



#   ==========================================
#           Launching bot

client.run(settings['private']['token'])