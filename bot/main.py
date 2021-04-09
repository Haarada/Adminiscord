from imports import *

token = configHandler.configHandle().loadCfg()
words = loadWords.loadWords().lw()
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith('.test'):
        await message.channel.send('Testing!')

    print(msg)
    msg = msg.lower()
    for word in words:
        if word in msg:
            msg = msg.replace(word,"\*"*len(word))
            await message.channel.send(message.author.mention+" Watch your language! Censored message:\n> "+msg)
            await message.delete()

    print(msg)

client.run(token['private']['token'])