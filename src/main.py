from imports import *

token = cH.configHandle().loadCfg()
words = lW.loadWords().lw()
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith('test'):
        await message.channel.send('Testing!')

    # ==== \/ zapisywanie wiadomosci do pliku \/ ====
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

    #print(msg)

client.run(token['private']['token'])