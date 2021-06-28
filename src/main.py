from imports import *

settings = fH.fileHandler().loadCfg()
datafile = fH.fileHandler().loadData()
words = lW.loadWords().lw()


intents = discord.Intents.default()
#intents.members = True

client = commands.Bot('!', intents=intents)




#   ========================================
#           On Ready event

@client.event
async def on_ready():

    print('Logged in as {0.user}'.format(client))
    print('to stop bot write in the chat:', "STOP_"+client.user.discriminator)
    print("You have to be owner of the bot to do that.")


#   ========================================
#           On message event

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print("author id:",message.author.id)

    msg = message.content
    if msg.startswith('test'):
        await message.channel.send('Testing!')
        
        # ==== \/ exiting the bot \/ ====
    if str(message.author.id) == str(settings['private']['owner_id']) and message.content == "STOP_"+client.user.discriminator:
        fH.fileHandler().saveData(datafile)
        print("Adminiscord is closing...")
        exit()

    # ==== \/ saving messages to file \/ ====
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")

    if  os.path.exists(".\\data\\messages\\"+str(message.guild.id)+".txt"):
        logchat = open(".\\data\\messages\\"+str(message.guild.id)+".txt","a")  # Open in Append mode
    else:
        logchat = open(".\\data\\messages\\"+str(message.guild.id)+".txt","x")  # open in Write mode (with file creation)
        
    logchat.write("["+time+"]["+message.channel.name+"]["+message.author.mention+"]["+msg+"]\n") 
    logchat.close()

    print("["+time+"]["+message.channel.name+"]["+message.author.display_name+"]["+msg+"]")
    msg = msg.lower()
    deleteword = False
    for word in words:
        if word in msg:
            msg = msg.replace(word,"\*"*len(word))
            deleteword = True
            
    if deleteword == True:
        await message.channel.send(message.author.mention+" Watch your language! Censored message:\n> "+msg)
        await message.delete()
        deleteword = False
    
    await client.process_commands(message)

    #print(msg)


#   ==========================================
#           Commands

client.run(settings['private']['token'])