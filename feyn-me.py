from discord.ext import commands
import discord

TOKEN ='MTE2NTQ4MzQ5MDc4NDA1NTM0Ng.Gvq9mU.lr91eTOG3HX-SRyPmROxUJzGlQxs0h3D4I3pws'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

clients = []
flag = 0
i = 0
@client.event
async def on_message(message):
    global flag
    global client
    global i
    msg = str(message.content)
    
    if message.author == client.user:
        return
    
    print(message.author)
    print(clients)
    if msg == "-start session":
        await message.channel.send("Join the Feyn-Me Session!")
        flag = 1
    
    if(flag == 1 and msg == "-join" and not(message.author.name in clients)):
        await message.channel.send(message.author.name + " Joined the Session")
        i+=1
        clients.append(message.author.name)
        print(clients)

    start = msg.split()
    print(start)
    if(len(start) == 3):
        if(flag == 1 and start[0] == "-start" and start[1] == "-t"):
            await message.channel.send("Feyn-me Session has Started!\nThe Topic is: "+start[2])



client.run(TOKEN)
    