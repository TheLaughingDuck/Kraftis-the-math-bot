import discord
import os

#Create an instance of a client
#Intents specification required apparently
intents = discord.Intents.all()
client = discord.Client(intents=intents)


# EVENT on START
@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))
    
    #channel = client.get_channel() #Put "channel-number" in parentheses
    #await channel.send("I have been deployed!")


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


# RUN the CLIENT
#client.run(os.environ["KEY1"], bot=True)