import discord
import os
from dotenv import load_dotenv

from math_package import *

#Create an instance of a client
#Intents specification required apparently
intents = discord.Intents.all()
client = discord.Client(intents=intents)


# EVENT on START
@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))
    
    dev_channel = client.get_channel(997984431883173958)
    await dev_channel.send("I have been deployed!")


# EVENT on MESSAGE
@client.event
async def on_message(message):
    if(message.author == client.user):
        return

    # GREET A USER
    if message.content == 'hello':
        await message.channel.send("Hello!")

    # PRESENT THE AVAILABLE COMMANDS
    if message.content == "help":
        help_message = "Theses are my commands:\n"
        help_message+= "------------------------\n"
        help_message+= "hello: Greets you in a friendly manner\n"
        help_message+= "help: Shows this message\n"

        await message.channel.send("```" + help_message + "```")
    
    if message.content.startswith("kräftis calc"):
        text = message.content.replace("kräftis calc ", "")
        result = main.evaluate(text)

        await message.channel.send(text + " = " + str(result))


# RUN the CLIENT
load_dotenv()
client.run(os.getenv("KEY1"), bot=True)